$(document).ready(function() {
    function updateDisplay(arene) {
        $(`#cbt_rouge_carton_blanc`).text(arene["cartons"]["rouge"]["blanc"]);
        $(`#cbt_rouge_carton_jaune`).text(arene["cartons"]["rouge"]["jaune"]);
        $(`#cbt_rouge_carton_rouge`).text(arene["cartons"]["rouge"]["rouge"]);
        $(`#cbt_vert_carton_blanc`).text(arene["cartons"]["vert"]["blanc"]);
        $(`#cbt_vert_carton_jaune`).text(arene["cartons"]["vert"]["jaune"]);
        $(`#cbt_vert_carton_rouge`).text(arene["cartons"]["vert"]["rouge"]);

        $(`#score_rouge`).text(arene["score"]["rouge"]);
        $(`#score_vert`).text(arene["score"]["vert"]);
    }

    $('.score-button').click(function() {
        const color = $(this).data('color');
        const value = $(this).data('value');
        const id_arene = $(this).data('arene');

        $.post(`/increment-score/${id_arene}/${color}/${value}`, function(data) {
            updateDisplay(data.arene);
            addHistoryLine(color, data.arene.historique[data.arene.historique.length-1]);
        });
    });

    $('.carton-button').click(function() {
        const color = $(this).data('color');
        const value = $(this).data('value');
        const id_arene = $(this).data('arene');

        $.post(`/increment-carton/${id_arene}/${color}/${value}`, function(data) {
            updateDisplay(data.arene);
            addHistoryLine(color, data.arene.historique[data.arene.historique.length-1]);
        });
    });

    $('.annuler').click(function() {
        const id_arene = $(this).data('arene');

        $.post(`/annuler/${id_arene}`, function(data) {
            updateDisplay(data.arene);
            $('.history_line:first').remove();
        });
    });

    function addHistoryLine(color, action) {
        const html_line = `
            <div class="history_line">
                <span class="history-timestamp">${action[0]}</span>
                <span class="history-category ${action[1]}">${action[1]}</span>: 
                <span class="history-details">${action[2]} ${action[3]}</span>
            </div>`;

        $('#actions-list').prepend(html_line);
    }

    ///////////////////// TIMER /////////////////////
    const timerValue = document.getElementById('timer-value');

    const id_arene = $('.hidden').data('value');

    function updateTimerDisplay() {
        $.post(`/infos/${id_arene}`, function(data) {
            let minutes = Math.floor(data.arene.remaining_time / 60).toString().padStart(2, '0');
            let seconds = (data.arene.remaining_time % 60).toString().padStart(2, '0');
            timerValue.textContent = `${minutes}:${seconds}`;
        });
    }

    function startTimer() {
        $.post(`/start-timer/${id_arene}`, function(data) {});
    }

    function pauseTimer() {
        $.post(`/pause-timer/${id_arene}`, function(data) {});
    }

    function resetTimer() {
        $.post(`/reset-timer/${id_arene}`, function(data) {});
    }

    function incTimer() {
        // ajouter 5 secondes
        $.post(`/add-seconds/${id_arene}/5`, function(data) {});
    }

    function decTimer() {
        // enlever 5 secondes
        $.post(`/sub-seconds/${id_arene}/5`, function(data) {});
    }

    const playBtn = document.getElementById('start-button');
    const pauseBtn = document.getElementById('pause-button');
    const resetBtn = document.getElementById('reset-button');
    const plusBtn = document.getElementById('plus-button');
    const minusBtn = document.getElementById('minus-button');
    // Event listeners for buttons
    playBtn.addEventListener('click', startTimer);
    pauseBtn.addEventListener('click', pauseTimer);
    resetBtn.addEventListener('click', resetTimer);
    plusBtn.addEventListener('click', incTimer);
    minusBtn.addEventListener('click', decTimer);

    setInterval(() => {updateTimerDisplay();}, 500);
});
