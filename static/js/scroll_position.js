// Function to save scroll position
function saveScrollPosition() {
    sessionStorage.setItem('scrollPosition', window.scrollY);
}

// Function to restore scroll position
function restoreScrollPosition() {
    let scrollPosition = sessionStorage.getItem('scrollPosition');
    if (scrollPosition !== null) {
        $(window).scrollTop(parseInt(scrollPosition));
        sessionStorage.removeItem('scrollPosition');
    }
}

// Restore scroll position when the page loads
$(document).ready(function () {
    restoreScrollPosition();
});

// Save scroll position before form submission
$(document).on('change', '#sort_by', function () {
    saveScrollPosition();
    $(this).closest('form').submit();
});