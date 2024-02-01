from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/projects')
def index():
    return render_template("projects.html")

@app.route('/loading')
def index():
    return render_template("loading.html")

@app.route('/aboutme')
def index():
    return render_template("aboutme.html")

@app.route('/projects/page')
def index():
    return render_template("projectPage.html")



if __name__ == "__main__":
    app.run(debug=True)

# les feuilles de style, scripts, images et autres éléments qui ne seront jamais générés dynamiquement doivent être dans le dossier static,
# les fichiers HTML doivent être dans le dossier templates,
# les tests doivent être dans le dossier tests,
# le fichier views.py contient les différentes routes de l'application