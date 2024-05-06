from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/projects')
def projects():
    return render_template("projects.html")

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(port=3003)

# les feuilles de style, scripts, images et autres éléments qui ne seront jamais générés dynamiquement doivent être dans le dossier static,
# les fichiers HTML doivent être dans le dossier templates,
# les tests doivent être dans le dossier tests,
# le fichier views.py contient les différentes routes de l'application
