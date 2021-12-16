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


    $('#genre').on('change', function(){
        url = '/music_item/' + this.value;
        $("#music_items_selector option").each(function() {
            $(this).remove();
        });
        $.get( url, function( data ) {
            arrayData = data['music_items'];
            for (var i = 0; i < arrayData.length; i++) {
                $('#music_items_selector').append(
                    '<option value="' + arrayData[i].title + '">' + arrayData[i].genre_name + ' : ' + arrayData[i].title + '</option>');
            }
            $('#music_items_selector').formSelect();
        
        });

    });
});
