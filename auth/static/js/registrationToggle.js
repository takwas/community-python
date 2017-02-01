$(document).ready(function() {
    $('#toggle-registration').on('click', function(e) {
        $('.content-section').toggleClass('show')

        var text = $(e.target).text();

        $(e.target).text(text == 'Registreren' ? 'Sluiten' : 'Registreren')
    })
})