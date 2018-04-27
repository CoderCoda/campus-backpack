$(document).ready(function() {
    $('.navbar').affix({
        offset: {
            top: $('.header').height()
        }
    });
});