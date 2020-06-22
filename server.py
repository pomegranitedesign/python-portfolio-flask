import csv
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def blog():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name: str):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()  # Creates a dict from all the front end form data
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong, try again'


# Helpers
def write_to_database(data: dict):
    with open('database.txt', 'a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')


def write_to_csv(data: dict):
    with open('database.csv', 'a', newline='\n') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(
            database2, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
