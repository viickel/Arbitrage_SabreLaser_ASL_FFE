$(document).ready(function() {
    $('.increment-score').click(function() {
        const color = $(this).data('color');
        const value = $(this).data('value');

        $.post(`/increment-score/${color}/${value}`, function(data) {
            $(`#score_${color}`).text(data.score[color]);
            addHistoryLine(color, data.last_action)
        });
    });

    $('.increment-carton').click(function() {
        const color = $(this).data('color');
        const value = $(this).data('value');

        $.post(`/increment-carton/${color}/${value}`, function(data) {
            $(`#cbt_${color}_carton_${value}`).text(data.cartons[color][value]);
            $(`#score_rouge`).text(data.score["rouge"]);
            $(`#score_vert`).text(data.score["vert"]);
            addHistoryLine(color, data.last_action)
        });
    });

    $('.annuler').click(function() {
        $.post(`/annuler/1`, function(data) {
            $(`#cbt_rouge_carton_blanc`).text(data.cartons["rouge"]["blanc"]);
            $(`#cbt_rouge_carton_jaune`).text(data.cartons["rouge"]["jaune"]);
            $(`#cbt_rouge_carton_rouge`).text(data.cartons["rouge"]["rouge"]);
            $(`#cbt_vert_carton_blanc`).text(data.cartons["vert"]["blanc"]);
            $(`#cbt_vert_carton_jaune`).text(data.cartons["vert"]["jaune"]);
            $(`#cbt_vert_carton_rouge`).text(data.cartons["vert"]["rouge"]);

            $(`#score_rouge`).text(data.score["rouge"]);
            $(`#score_vert`).text(data.score["vert"]);
            $('#liste_historique .ligne_historique:first').remove();
        });
    });

    function addHistoryLine(color, line) {
        const html_line = `<div class="ligne_historique ${color}">${line}</div>`;
        $('#liste_historique').prepend(html_line);
    }
});
