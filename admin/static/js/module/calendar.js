$(document).ready(function() {
    $('#module_calendar').fullCalendar({
        header: {
            left: 'prev, next today',
            center: 'title',
            right: 'month'
        },
        events: '/admin/api/modules/module/' + $('#module_calendar').data('module-uuid') +'/locations'
    })
})