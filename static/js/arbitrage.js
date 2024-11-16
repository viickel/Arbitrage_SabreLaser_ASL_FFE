$(document).ready(function() {
    $('#buttonRouge1').click(function() {
        $.post('/increment', function(data) {
            $('#counter').text(data.score_rouge);
        });
    });
});




// // Fonction de mise à jour du score sur l'interface
// function majScoreDisplay(combattant, score) {
//     if (combattant === 'Vert') {
//         document.getElementById('scoreVert').textContent = score;
//     } else if (combattant === 'Rouge') {
//         document.getElementById('scoreRouge').textContent = score;
//     }
// }

// const socket = io();
// const num_arene = "{{ num_arene }}";

// // Envoi de la mise à jour au serveur
// function majScore(combattant, valeur) {
//     socket.emit('maj_score', { combattant, valeur });
// }

// // Mise à jour depuis le serveur
// socket.on('score_updated', function(data) {
//     majScoreDisplay(data.combattant, data.score);
// });

// // Variables et boutons pour la détection d'appui court/long
// const btn1ptvert = document.getElementById('buttonVert1');
// let pressTimer;

// // Appui court - ajouter 1 point
// btn1ptvert.addEventListener('click', function () {
//     majScore('Vert', 1);
// });

// // Appui long - retirer 1 point
// btn1ptvert.addEventListener('mousedown', function () {
//     pressTimer = setTimeout(function() {
//         majScore('Vert', -1);
//     }, 800); // 800 ms pour détecter un appui long
// });

// // Annuler l'appui long si le bouton est relâché ou si la souris quitte le bouton
// btn1ptvert.addEventListener('mouseup', function() {
//     clearTimeout(pressTimer);
// });

// btn1ptvert.addEventListener('mouseleave', function() {
//     clearTimeout(pressTimer);
// });