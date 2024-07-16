$(document).ready(function() {
  var form = $('#mc-embedded-subscribe-form');
  var emailInput = $('#mce-EMAIL');
  var errorDiv = $('#mce-error-response');

  form.on('submit', function(event) {
    if (!emailInput[0].checkValidity()) {
      event.preventDefault();  // Prevent form submission
      emailInput[0].setCustomValidity("Please enter a valid email address.");
      errorDiv.show().text(emailInput[0].validationMessage);
    } else {
      clearError();  // Clear any previous error messages
    }
  });

  emailInput.on('input', function() {
    if (emailInput[0].checkValidity()) {
      clearError();
    }
  });

  function clearError() {
    emailInput[0].setCustomValidity("");
    errorDiv.hide().text('');
  }
});