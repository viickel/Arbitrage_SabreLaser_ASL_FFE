# Application d'arbitrage sabre laser
Cette application web est developpée dans un environnement python avec Flask. Son but est dans un premier temps de créer une interface d'arbitrage au sabre laser.
La structure des pages est la suivante :
+ Page arbitrage : Permet la saisie des scores du match en cours et la gestion d'un chronomètre
+ Page affichage : Affichage des scores et du chronomètre sur une TV connectée via navigateur en réseau local
+ Bandeau : Page web spécifique pour l'integration d'un bandeau (en live par exemple via OBS) avec le score et le nom des combattants
+ Config : Page de configuration pour paramétrer les noms des combatants sur les arènes à distance

L'application doit pour le moment fonctionner de manière indépendante. Par exemple, la modification du nom des combattant se ferait dans la page de configuration.
Par contre, dans les dictionnaires de données je prévois déjà des variables comme le numero de licence pour relier à une base de données ou bien les points quest pour enregistrer les match.
