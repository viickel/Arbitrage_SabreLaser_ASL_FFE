# Comment utiliser l'application 
Après avoir démarer l'application dans votre editeur Python on peut utiliser plusieurs pages web  : 
+ Adresse_Ip_du_PC:5000/configuration - Permet d'ajouter ou de supprimer des arene, remet a zero les points sur une arene et changer les noms des combatants
+ Adresse_Ip_du_PC:5000//Arene/XX - Remplacer le XX par le numero d'arene, cette interface permet aux e-arbitre de gérer les match
+ Adresse_Ip_du_PC:5000//affichage/XX - Remplacer le XX par le numéro de l'arene, cette interface permet d'afficher le scores en direct
+ Adresse_Ip_du_PC:5000//bandeau/XX - Remplacer le XX par le numéro de l'arene, cette interface permet d'afficher le scores en direct sous la forme d'un bandeau pour une interface de steam

  
# Application d'arbitrage sabre laser
Cette application web est developpée dans un environnement python avec Flask. Son but est dans un premier temps de créer une interface d'arbitrage au sabre laser.
La structure des pages est la suivante :
+ Page arbitrage : Permet la saisie des scores du match en cours et la gestion d'un chronomètre
+ Page affichage : Affichage des scores et du chronomètre sur une TV connectée via navigateur en réseau local
+ Bandeau : Page web spécifique pour l'integration d'un bandeau (en live par exemple via OBS) avec le score et le nom des combattants
+ Config : Page de configuration pour paramétrer les noms des combatants sur les arènes à distance

L'application doit pour le moment fonctionner de manière indépendante. Par exemple, la modification du nom des combattant se ferait dans la page de configuration.
Par contre, dans les dictionnaires de données je prévois déjà des variables comme le numero de licence pour relier à une base de données ou bien les points quest pour enregistrer les match.

## Structures de données
Les objets manipulés par l'interface web sont les arènes et les combattants, rassemblés dans une compétition.
Ces objets python possèdent les attributs et méthodes suivants :

### Compétition
- arenes

### Arène
- numero
- combattants
- score
- cartons
- historique
- ajouterCarton(combattant, couleur)
- incrementerScore(combattant, increment)
- annulerDerniereAction

### Combattant
- nom
- license
- points_quest
