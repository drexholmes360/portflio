from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

def save_user_info(data):
    with open("database.csv", 'a+', newline='') as this_file:
        email = data['this_email']
        subject = data['this_subject']
        message = data['this_message']
        # write to the file
        csv_file = csv.writer(this_file, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)
        csv_file.writerow([email, subject, message])

# homepage
@app.route('/')
def home_without_route():
    return render_template("index.html")

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        save_user_info(data)
        print('CLIENT REPORT 200: form submited')
        return redirect("thankyou.html")
    else:
        print('CLIENT REPORT 400: from not submited')

