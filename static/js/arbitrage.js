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

    $('.increment-score').click(function() {
        const color = $(this).data('color');
        const value = $(this).data('value');
        const id_arene = $(this).data('arene');

        $.post(`/increment-score/${id_arene}/${color}/${value}`, function(data) {
            updateDisplay(data.arene);
            addHistoryLine(color, data.arene.historique[data.arene.historique.length-1]);
        });
    });

    $('.increment-carton').click(function() {
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

    let timerDuration = 210; // in seconds
    let timeLeft = timerDuration;
    let timerInterval;
    let isRunning = false;

    const timerValue = document.getElementById('timer-value');
    const playBtn = document.getElementById('start-button');
    const pauseBtn = document.getElementById('pause-button');
    const resetBtn = document.getElementById('reset-button');
    const plusBtn = document.getElementById('plus-button');
    const minusBtn = document.getElementById('minus-button');

    function updateTimerDisplay() {
        let minutes = Math.floor(timeLeft / 60).toString().padStart(2, '0');
        let seconds = (timeLeft % 60).toString().padStart(2, '0');
        timerValue.textContent = `${minutes}:${seconds}`;

        // Enable or disable the clickable button based on timeLeft
        plusBtn.disabled = isRunning == true;
        minusBtn.disabled = isRunning == true;
    }

    function startTimer() {
        if (!isRunning) {
            timerInterval = setInterval(() => {
                if (timeLeft > 0) {
                    timeLeft--;
                    updateTimerDisplay();
                } else {
                    clearInterval(timerInterval);
                    isRunning = false;
                }
            }, 1000);
            isRunning = true;
        }
    }

    function pauseTimer() {
        clearInterval(timerInterval);
        isRunning = false;
        updateTimerDisplay();
    }

    function resetTimer() {
        clearInterval(timerInterval);
        timeLeft = timerDuration;
        isRunning = false;
        updateTimerDisplay();
    }

    function incTimer() {
        timeLeft += 5;
        updateTimerDisplay();
    }

    function decTimer() {
        timeLeft -= 5;
        updateTimerDisplay();
    }

    // Event listeners for buttons
    playBtn.addEventListener('click', startTimer);
    pauseBtn.addEventListener('click', pauseTimer);
    resetBtn.addEventListener('click', resetTimer);
    plusBtn.addEventListener('click', incTimer);
    minusBtn.addEventListener('click', decTimer);

    // Initialize display on load
    updateTimerDisplay();
});
