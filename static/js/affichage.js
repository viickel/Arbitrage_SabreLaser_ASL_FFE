function updateDisplay() {
    const id_arene = $('.hidden').data('value');

    $.post(`/infos/${id_arene}`, function(data) {
        $(`#score_rouge`).text(data.arene["score"]['rouge']);
        $(`#score_vert`).text(data.arene["score"]['vert']);
        
        $(`#cbt_rouge_carton_blanc`).text(data.arene['cartons']['rouge']['blanc']);
        $(`#cbt_rouge_carton_jaune`).text(data.arene['cartons']['rouge']['jaune']);
        $(`#cbt_rouge_carton_rouge`).text(data.arene['cartons']['rouge']['rouge']);
        $(`#cbt_vert_carton_blanc`).text(data.arene['cartons']['vert']['blanc']);
        $(`#cbt_vert_carton_jaune`).text(data.arene['cartons']['vert']['jaune']);
        $(`#cbt_vert_carton_rouge`).text(data.arene['cartons']['vert']['rouge']);
    });
}

setInterval(() => {updateDisplay();}, 500);