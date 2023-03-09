from flask import Flask, render_template, request, jsonify
from summarization.extractive import summarize_extractive
from summarization.abstractive import summarize_abstractive

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('extractive.html')

@app.route('/extractive', methods=['GET', 'POST'])
def extractive():
    if request.method == 'POST':
        text = request.form['text']
        if not text:
            return render_template('error.html', error='Please provide text to summarize.')
        summary = summarize_extractive(text)
        return render_template('extractive.html', summary=summary)
    return render_template('extractive.html')


@app.route('/abstractive', methods=['GET', 'POST'])
def abstractive():
    if request.method == 'POST':
        text = request.form['text']
        if not text:
            return render_template('error.html', error='Please provide text to summarize.')
        summary = summarize_abstractive(text)
        return render_template('abstractive.html', summary=summary)
    return render_template('abstractive.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', error='Page not found.'), 404



@app.errorhandler(500)
def internal_server_error(error):
    return render_template('error.html', error='Internal server error.'), 500

if __name__ == '__main__':
    app.run(debug=True)
