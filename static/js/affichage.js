function updateDisplay() {
    const id_arene = $('.hidden').data('value');

    $.post(`/score/${id_arene}`, function(data) {
        // pour l'instant, ne fonctionne qu'avec
        // une seule arène
        $(`#score_rouge`).text(data.score['rouge']);
        $(`#score_vert`).text(data.score['vert']);
    });
}

setInterval(() => {updateDisplay();}, 500);