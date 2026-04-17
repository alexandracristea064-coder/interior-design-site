from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# 👇 FORȚĂM SERVIREA STATIC
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(os.path.join(app.root_path, 'static'), filename)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

if __name__ == '__main__':
    app.run(debug=True)