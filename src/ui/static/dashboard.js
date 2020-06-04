$('div.dropdown-menu > a').click( function(e) {
    e.preventDefault();
    name = $(this).attr('id').split('-')[1]

    // remove all active classes from nav tabs
    $('div .nav-tabs > a').removeClass('active')
    $('div .nav-tabs > div.dropdown > a').removeClass('active')

    // set this group as the active tab
    $(this).parent().siblings('a').addClass('active')

    // update the image
    $('#imageHolder').attr('src', '/static/graph/' + name + '.png')
} )
