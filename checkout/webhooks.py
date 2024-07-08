from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.webhook_handler import StripeWH_Handler

import stripe

@require_POST
@csrf_exempt
def webhook(request):
    """
    Listen for and handle Stripe webhooks.

    This function sets up Stripe's webhook listener to handle different types 
    of events sent by Stripe to the webhook endpoint. It validates the payload 
    and signature of the incoming webhook request, and dispatches the event 
    to the appropriate handler.

    Args:
        request (HttpRequest): The incoming HTTP request containing the 
            webhook payload and headers.

    Returns:
        HttpResponse: A response with the status code indicating the result 
            of processing the webhook event.
    """
    # Setup Stripe API key and webhook secret
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Retrieve the webhook payload and signature header from the request
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        # Verify the webhook signature and construct the event object
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        # Return a 400 error for invalid payloads
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Return a 400 error for invalid signatures
        return HttpResponse(status=400)
    except Exception as e:
        # Return a 400 error for any other exceptions
        return HttpResponse(content=e, status=400)

    # Initialize the webhook handler
    handler = StripeWH_Handler(request)

    # Map specific Stripe event types to their corresponding handler methods
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,
    }

    # Determine the event type from the Stripe event object
    event_type = event['type']

    # Get the handler for the specific event type, or use the generic handler
    event_handler = event_map.get(event_type, handler.handle_event)

    # Process the event using the determined handler
    response = event_handler(event)
    return response
