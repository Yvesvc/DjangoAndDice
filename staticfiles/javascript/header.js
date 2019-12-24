
/* Alert window size too big */
$(document).ready(function(){

    var window_width = $(window).width();
    var window_height = $(window).height();
    var current_path = window.location.pathname;


    if ((window_width > 700 || window_height > 1000) && current_path.indexOf('user/login') >=0) {
    alert ('Django and Dice is created for small devices, you might consider switching to a smaller device.');
    }

});