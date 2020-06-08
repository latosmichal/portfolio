from flask import Flask, render_template, request, send_from_directory
import os
import csv
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/<string:page>')
def html_page(page):
    return render_template(page)


@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return 'Form submitted'
        except:
            return 'did not save to db'
    else:
        return 'Sth went wrong'

def write_to_db(data):
    with open('database.txt', mode='a') as database:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{name}, {email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,subject,message])


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')