function updateTimerDisplay() {
    $.post(`/score/1`, function(data) {
        // pour l'instant, ne fonctionne qu'avec
        // une seule arène
        $(`#score_rouge`).text(data.score['rouge']);
        $(`#score_vert`).text(data.score['vert']);
    });
}

setInterval(() => {updateTimerDisplay();}, 500);