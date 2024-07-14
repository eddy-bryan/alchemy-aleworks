// JavaScript code derived from Boutique Ado

// Check if a country is initially selected
let countrySelected = $('#id_default_customer_country').val();

// If no country is selected initially, set the text colour to a muted colour
if(!countrySelected) {
    $('#id_default_customer_country').css('color', '#aab7c4');
}

// Listen for changes in the country selection dropdown
$('#id_default_customer_country').change(function() {
    // Update the selected country
    countrySelected = $(this).val();

    // If no country is selected after change, set text colour to muted; otherwise, set it to black
    if(!countrySelected) {
        $(this).css('color', '#aab7c4'); // Muted color
    } else {
        $(this).css('color', '#000000'); // Black color
    }
});