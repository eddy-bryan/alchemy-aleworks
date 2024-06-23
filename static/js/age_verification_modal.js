// Age Verification Modal cookie logic is a modified version of a code snippet taken from 'https://www.digital.ink/blog/age-verification-modal/'.
$(document).ready(function () {
    // Function to create a cookie
    function createCookie(name, value, days) {
        var expires = "";
        if (days) {
            var date = new Date();
            date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
            expires = "; expires=" + date.toUTCString();
        }
        document.cookie = name + "=" + value + expires + "; path=/";
        console.log("Cookie created:", name, value); // For debugging
    }

    // Function to read a cookie
    function readCookie(name) {
        var nameEQ = name + "=";
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.indexOf(nameEQ) === 0) {
                return cookie.substring(nameEQ.length, cookie.length);
            }
        }
        return null;
    }

    // Check for the cookie and show/hide modal accordingly
    if (readCookie('age_check') === 'true') {
        $('#exampleModalCenter').modal('hide');
    } else {
        $('#exampleModalCenter').modal({
            backdrop: 'static', // Prevent closing on backdrop click
            keyboard: false // Prevent closing with keyboard Esc key
        });
    }

    // Set the cookie when the "Yes" button is clicked and hide the modal
    $('#age-verify-button').click(function () {
        createCookie('age_check', 'true', 1);
        $('#exampleModalCenter').modal('hide');
    });
});
