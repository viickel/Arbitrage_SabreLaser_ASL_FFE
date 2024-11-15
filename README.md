# Application d'arbitrage sabre laser
Cette application est developper dans un environement python avec Flask, le but est dans un premier temps de créer une interface d'arbitrage au sabre laser avec des pages structutrer comme ceci 
+ Page arbitrage : Permet de rentrés les scores du match en cours et de gérer un chronometre
+ Page Affichage : Affichage des score et du chrono sur une tv connecter via le navigateur en reseau local
+ Bandeau : Une page web pour integrer un bandeau avec le scrore et le nom des combatant sur un live par exemple avec OBS
+ Config : une page de config pour configurer les nom des combatant sur les arene a distance


L'application doit pour le moment fonctionner de maniere indépendante, par exemple la modification du nom des combatant se ferais dans la page de config, par contre dans les dictionnaire de donné je prévois deja des variable comme le numero de licencen pour relier a une base de donnée ou bien les points quest pour enregistrer les match.