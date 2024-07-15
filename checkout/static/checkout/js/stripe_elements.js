/*
    Core logic/payment flow originally adapted from Boutique Ado project,
    which in turn derives from:
    https://stripe.com/docs/payments/accept-a-payment

    CSS styling based on:
    https://stripe.com/docs/stripe-js
*/
document.addEventListener('DOMContentLoaded', function() {
    // Extracting Stripe public key and client secret from HTML
    var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
    var clientSecret = $('#id_client_secret').text().slice(1, -1);
    
    // Initialise Stripe.js with the public key
    var stripe = Stripe(stripePublicKey);
    var elements = stripe.elements();
    
    // Custom styling for Stripe elements
    var style = {
        base: {
            color: '#000000',
            fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
            fontSmoothing: 'antialiased',
            fontSize: '16px',
            '::placeholder': {
                color: '#aab7c4'
            }
        },
        invalid: {
            color: '#dc3545',
            iconColor: '#dc3545'
        }
    };

    // Create a Card Element with custom styling
    var card = elements.create('card', {style: style});
    card.mount('#card-element');

    // Handle realtime validation errors on the card element
    card.addEventListener('change', function (event) {
        var errorDiv = document.getElementById('card-errors');
        if (event.error) {
            // Display error message
            var html = `
                <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                </span>
                <span>${event.error.message}</span>
            `;
            $(errorDiv).html(html);
        } else {
            // Clear error message
            errorDiv.textContent = '';
        }
    });

    // Handle form submission
    var form = document.getElementById('payment-form');
    
    form.addEventListener('submit', function(ev) {
        ev.preventDefault();
        
        // Disable card element and submit button
        card.update({ 'disabled': true});
        $('#submit-button').attr('disabled', true);
        
        // Toggle loading overlay
        $('#payment-form').fadeToggle(100);
        $('#loading-overlay').fadeToggle(100);

        // Determine if user wants to save information to profile
        var saveInfo = Boolean($('#id-save-info').attr('checked'));
        
        // Retrieve CSRF token from form
        var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
        
        // Prepare data to post to server for cache checkout data
        var postData = {
            'csrfmiddlewaretoken': csrfToken,
            'client_secret': clientSecret,
            'save_info': saveInfo,
        };
        var url = '/checkout/cache_checkout_data/';
    
        // Post data to server and handle response
        $.post(url, postData).done(function () {
            // Confirm payment with Stripe
            stripe.confirmCardPayment(clientSecret, {
                payment_method: {
                    card: card,
                    billing_details: {
                        name: $.trim(form.customer_name.value),
                        phone: $.trim(form.customer_phone.value),
                        email: $.trim(form.customer_email.value),
                        address:{
                            line1: $.trim(form.customer_address1.value),
                            line2: $.trim(form.customer_address2.value),
                            city: $.trim(form.customer_city.value),
                            country: $.trim(form.customer_country.value),
                            state: $.trim(form.customer_county.value),
                        }
                    }
                },
                shipping: {
                    name: $.trim(form.customer_name.value),
                    phone: $.trim(form.customer_phone.value),
                    address: {
                        line1: $.trim(form.customer_address1.value),
                        line2: $.trim(form.customer_address2.value),
                        city: $.trim(form.customer_city.value),
                        country: $.trim(form.customer_country.value),
                        postal_code: $.trim(form.customer_postcode.value),
                        state: $.trim(form.customer_county.value),
                    }
                },
            }).then(function(result) {
                if (result.error) {
                    // Display error message
                    var errorDiv = document.getElementById('card-errors');
                    var html = `
                        <span class="icon" role="alert">
                        <i class="fas fa-times"></i>
                        </span>
                        <span>${result.error.message}</span>`;
                    $(errorDiv).html(html);
                    
                    // Toggle form and loading overlay visibility
                    $('#payment-form').fadeToggle(100);
                    $('#loading-overlay').fadeToggle(100);
                    
                    // Re-enable card element and submit button
                    card.update({ 'disabled': false});
                    $('#submit-button').attr('disabled', false);
                } else {
                    if (result.paymentIntent.status === 'succeeded') {
                        // If payment succeeded, submit the form
                        form.submit();
                    }
                }
            });
        }).fail(function () {
            // Reload the page if there's an error (error message will be in Django messages)
            location.reload();
        })
    });
});
