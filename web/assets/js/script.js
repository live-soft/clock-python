eel.setInterval();

eel.expose(clock)
function clock(seconds, minutes, hourse) {
    $('.seconds-arrow').css('transform', `rotate(${ seconds }deg)`);
    $('.minutes-arrow').css('transform', `rotate(${ minutes }deg)`);
    $('.hourse-arrow').css('transform', `rotate(${ hourse }deg)`);

    $('.seconds-arrow').css('display', 'block');
    $('.minutes-arrow').css('display', 'block');
    $('.hourse-arrow').css('display', 'block');

}