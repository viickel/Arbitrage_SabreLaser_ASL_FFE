function updateDisplay() {
    const id_arene = $('.hidden').data('value');

    $.post(`/infos/${id_arene}`, function(data) {
        $(`#nom_cbt_rouge`).text(data.arene.combattants["rouge"].nom);
        $(`#nom_cbt_vert`).text(data.arene.combattants["vert"].nom);

        $(`#score_rouge`).text(data.arene["score"]['rouge']);
        $(`#score_vert`).text(data.arene["score"]['vert']);
        
        $(`#cbt_rouge_carton_blanc`).text(data.arene['cartons']['rouge']['blanc']);
        $(`#cbt_rouge_carton_jaune`).text(data.arene['cartons']['rouge']['jaune']);
        $(`#cbt_rouge_carton_rouge`).text(data.arene['cartons']['rouge']['rouge']);
        $(`#cbt_vert_carton_blanc`).text(data.arene['cartons']['vert']['blanc']);
        $(`#cbt_vert_carton_jaune`).text(data.arene['cartons']['vert']['jaune']);
        $(`#cbt_vert_carton_rouge`).text(data.arene['cartons']['vert']['rouge']);

        let minutes = Math.floor(data.arene.remaining_time / 60).toString().padStart(2, '0');
        let seconds = (data.arene.remaining_time % 60).toString().padStart(2, '0');
        $(`#timer-value`).text(`${minutes}:${seconds}`);
    });
}

setInterval(() => {updateDisplay();}, 500);