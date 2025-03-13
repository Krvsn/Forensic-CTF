from flask import Flask, send_file, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/download')
def download_file():
    return send_file("secret.gz", as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
