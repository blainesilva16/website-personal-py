from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap5
from projects import projects
from contact_form import ContactForm
import os,dotenv,smtplib
import email_validator

dotenv.load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
EMAIL = os.getenv("EMAIL")

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("FLASK_KEY")
Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html', projects=projects)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET","POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        try:
            with smtplib.SMTP(HOST, 587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=EMAIL,
                    msg=f"Subject:A new message was sent to you!\n\nName: {name}\nEmail: {email}\nMessage: {message}")
        except:
            return render_template('contact.html', form=form, message="❌ Couldn't send your email, please try again.")
        else:
            return render_template("contact.html", form=form, message="✅ Message successfully sent!")
    return render_template("contact.html", form=form, message="Fill the form below.")

if __name__ == '__main__':
    app.run(debug=False)