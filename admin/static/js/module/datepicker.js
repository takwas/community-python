$(document).ready(function() {

    $("#start_datepicker" ).datepicker({
        dateFormat: "yy-mm-dd",
        onSelect: function(date) {
            const new_date = new Date(date)
            setStartDate(new_date)
        }
    });
    $("#end_datepicker" ).datepicker({
        dateFormat: "yy-mm-dd",
        defaultDate: new Date()
    });

    function setStartDate(date) {
        $("#end_datepicker").datepicker( "option", "minDate", date);
    }
})