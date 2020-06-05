$(document).ready(function() {
	// get current URL path and assign 'active' class
    var pathname = window.location.pathname;
    idx = pathname.indexOf('/', 1)
    if (idx > 0) {
        pathname = pathname.substring(0,idx)
    }
	$('nav > div > div > a[href="'+pathname+'"]').addClass('active');
})