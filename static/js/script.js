/*
    jQuery for MaterializeCSS initialization
*/

$(document).ready(function () {
    $(".sidenav").sidenav({edge: "right"});
    $(".collapsible").collapsible();
    $(".tooltipped").tooltip();
    $("select").formSelect();
    $(".datepicker").datepicker({
        format: "dd mmmm, yyyy",
        yearRange: 3,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });


    $('#music_title').on('change', function(){
        console.log(this.value);
        url = '/music_item/' + this.value;
        $.get( url, function( data ) {
            arrayData = data['music_items'];
            console.log(arrayData[0]);
            for (var i = 0; i < arrayData.length; i++) {
                $('#music_items_selector').append('<option value="' + arrayData[i]._id['$oid'] + '">' + arrayData[i].title + '</option>');
            }
            $('#music_items_selector').formSelect();
        
        });

    });
});
