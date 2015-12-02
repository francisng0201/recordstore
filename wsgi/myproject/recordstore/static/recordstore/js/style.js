$(function() {
    $('form').find(':input:not(button,[type="file"])').addClass('form-control');


    $('.block-search').on('keyup', function(e) {
        var search = $(this).val().toLowerCase().trim();

        $('.block-list').find('li').each(function() {
            var text = $(this).find('a').text().toLowerCase().trim();
            if (text.indexOf(search) < 0) {
                $(this).hide();
            } else {
                $(this).show();
            }
        });

    });
});
