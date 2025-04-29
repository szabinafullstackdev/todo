from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

teendok = []  # A teendők tárolására szolgáló lista

@app.route('/')
def index():
    """Megjeleníti a főoldalt a teendők listájával."""
    return render_template('index.html', teendok=teendok)

@app.route('/add', methods=['POST'])
def add_teendo():
    """Hozzáad egy új teendőt a listához."""
    teendo = request.form.get('teendo')
    if teendo:
        teendok.append(teendo)
    return redirect(url_for('index'))

@app.route('/delete/<int:teendo_index>', methods=['POST'])
def delete_teendo(teendo_index):
    """Töröl egy teendőt a listából."""
    if 0 <= teendo_index < len(teendok):
        teendok.pop(teendo_index)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)



if __name__ == "__main__":
    app.run(debug=True)
