$(document).ready(function() {
    $('.increment-score').click(function() {
        const color = $(this).data('color');
        const value = $(this).data('value');

        $.post(`/increment-score/${color}/${value}`, function(data) {
            $(`#score_${color}`).text(data.score[color]);
        });
    });

    $('.increment-carton').click(function() {
        const color = $(this).data('color');
        const value = $(this).data('value');

        $.post(`/increment-carton/${color}/${value}`, function(data) {
            $(`#cbt_${color}_carton_${value}`).text(data.cartons[color][value]);
            $(`#score_rouge`).text(data.score["rouge"]);
            $(`#score_vert`).text(data.score["vert"]);
        });
    });
});
