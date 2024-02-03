from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/projects')
def projects():
    return render_template("projects.html")

@app.route('/aboutme')
def aboutme():
    return render_template("aboutme.html")


def get_project_info(project_id):
    if project_id == 1:
        return {
            'title': 'VLD',
            'langages': {'JavaScript': '4.5%', 'NodeJS' : '15%', 'SQL' : '5%', 'html-5': '11.3%', 'css-3': '12.6%', 'python': '11.5%', 'EJS': '40.1%'},
            'description': 'VLD school est un projet de site internet en cours de développement, il proposera des formations sur des sujets informatiques tels que des cours sur Python, Blender, etc. Je mène ce projet en équipe avec Vrock691 & Davidbld.',
            'worktime': '1200h',
            'DevDate': '2023-2024',
            'Image' : 'logopngwhite.png',
            'Pictures' : ['VLD_screen1.png','VLD_screen2.png','VLD_screen3.png'],
            'status' : {'id': 'NotAllowed', 'text': 'Code non disponible'}
        }
    elif project_id == 2:
        return {
            'title': 'VAZ-Y',
            'langages': {'Flutter': '80%', 'Python': '10%', 'html-5': '10%'},
            'description': 'Le projet VAZ-Y est un projet d’application utilisant FLUTTER qui permet aux utilisateurs de commander des recettes en fonction des aliments qu’ils ont chez eux. Ne fonctionne pas car pas de partenaire...',
            'worktime': '40h',
            'DevDate': '2022',
            'Image' : 'VAZY.png',
            'Pictures' : [],
            'status': {'id': 'Allowed', 'text': 'Code disponible', 'link': 'https://github.com/Kez0X/VAZ-Y'}
        }
    elif project_id == 3:
        return {
            'title': 'SCRABBLE',
            'langages': {'Python': '100%'},
            'description': 'Le projet SCRABBLE est un projet de création du jeu scrabble avec toutes ses fonctionnalités en python : vérification des mots, multijoueur, mot triple, double...',
            'worktime': '20h',
            'DevDate': '2019',
            'Image' : 'Scrabble.webp',
            'Pictures' : [],
            'status': {'id': 'NotAllowed', 'text': 'Code non disponible'}
        }
    elif project_id == 4:
        return {
            'title': 'Simulateur de tournoi',
            'langages': {'Python': '100%'},
            'description': 'Le projet simulateur de tournoi est un simulateur de tournoi de foot avec les arbres grâce à python...',
            'worktime': '30h',
            'DevDate': '2020',
            'Image' : 'arbre.jpg',
            'Pictures' : [],
            'status': {'id': 'Allowed', 'text': 'Code disponible', 'link': 'https://github.com/Kez0X/Simulateur-Arbres/tree/main'}
        }
    elif project_id == 5:
        return {
            'title': 'La récursivité avec turtle',
            'langages': {'Python': '100%'},
            'description': "C'est un projet de lycée pour lequel on devait faire des formes grâce à la turtle de python et à la récursivité. Je vous laisse voir par vous-même.",
            'worktime': '20h',
            'DevDate': '2020',
            'Image' : 'turtle.jpg',
            'Pictures' : [],
            'status': {'id': 'Allowed', 'text': 'Code disponible', 'link': 'https://github.com/Kez0X/Python-Recursivit-'}
        }
    elif project_id == 6:
        return {
            'title': 'Social CO2',
            'langages': {'Flutter': '9%', 'Python': '28%', 'html-5': '9%', 'css-3': '9%', 'js': '9%', 'EJS': '9%', 'Firebase': '9%', 'SQL' : '9%' , 'ViewJS' : '9%'},
            'description': "C'est une application et un site web qui permettent de comparer sa production de CO2 avec celle de ses amis.",
            'worktime': '?h',
            'DevDate': '2024',
            'Image' : 'SCO2.svg',
            'Pictures' : [],
            'status': {'id': 'InLoad', 'text': 'En cours de création...'}
        }
    elif project_id == 7:
        return {
            'title': 'Support de cours',
            'langages': {'Python': '25%', 'html-5': '25%', 'css-3': '25%', 'js': '25%'},
            'description': "C'est un site avec un support de cours pour mes élèves de NSI.",
            'worktime': '60h',
            'DevDate': '2022',
            'Image' : 'livre.png',
            'Pictures' : [],
            'status': {'id': 'Allowed', 'text': 'Code disponible', 'link': 'https://github.com/Kez0X/SupportCourse'}
        }
    else:
        return None

@app.route('/projects/<project_id>')
def project_page(project_id):
    project_info = get_project_info(int(project_id))
    if project_info:
        return render_template("projectPage.html", project_info=project_info)
    else:
        return render_template("404.html"), 404


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404




if __name__ == "__main__":
    app.run(debug=True)

# les feuilles de style, scripts, images et autres éléments qui ne seront jamais générés dynamiquement doivent être dans le dossier static,
# les fichiers HTML doivent être dans le dossier templates,
# les tests doivent être dans le dossier tests,
# le fichier views.py contient les différentes routes de l'application