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


    let timerDuration = 210; // in seconds
    let timeLeft = timerDuration;
    let timerInterval;
    let isRunning = false;

    const timerDisplay = document.getElementById('timer-display');
    const playBtn = document.getElementById('play-btn');
    const pauseBtn = document.getElementById('pause-btn');
    const resetBtn = document.getElementById('reset-btn');
    const plusBtn = document.getElementById('plus-btn');
    const minusBtn = document.getElementById('minus-btn');

    function updateTimerDisplay() {
        let minutes = Math.floor(timeLeft / 60).toString().padStart(2, '0');
        let seconds = (timeLeft % 60).toString().padStart(2, '0');
        timerDisplay.textContent = `${minutes}:${seconds}`;

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
