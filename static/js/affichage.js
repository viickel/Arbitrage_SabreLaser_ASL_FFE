function updateDisplay() {
    const id_arene = $('.hidden').data('value');

    $.post(`/infos/${id_arene}`, function(data) {
        $(`#score_rouge`).text(data.arene["score"]['rouge']);
        $(`#score_vert`).text(data.arene["score"]['vert']);
        // TODO : ajouter le suivi des cartons
    });
}

setInterval(() => {updateDisplay();}, 500);