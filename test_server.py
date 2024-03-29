from flask import Flask, render_template
app = Flask(__name__)

@app.route("/", methods=('GET', 'POST'))
def test():
    return render_template('testing.html')

if __name__ == "__main__":
    app.debug=True
    app.run(host='0.0.0.0', port=80, debug=True)