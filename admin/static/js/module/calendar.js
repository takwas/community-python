$(document).ready(function() {
    $('#module_calendar').fullCalendar({
        header: {
            left: 'prev, next today',
            center: 'title',
            right: 'month, agendaWeek'
        },
        events: '/admin/api/modules/module/1/locations'
    })
})