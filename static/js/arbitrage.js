$(document).ready(function() {
    $('.increment-score').click(function() {
        const color = $(this).data('color');
        const value = $(this).data('value');

        $.post(`/increment/${color}/${value}`, function(data) {
            $(`#score_${color}`).text(data.score[color]);
        });
    });
});
