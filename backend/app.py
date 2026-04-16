from flask import Flask, render_template, request, redirect, flash
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
app.secret_key = "corevion_secret_key"

EMAIL_ADDRESS = "coreviontech@gmail.com"
EMAIL_PASSWORD = "japw klnh sdls nrdy"

@app.route("/")
def home():
    return render_template("contact.html")

@app.route("/send", methods=["POST"])
def send_email():
    try:
        name = request.form["name"]
        email = request.form["email"]
        number = request.form["number"]
        subject = request.form["subject"]
        message = request.form["message"]

        body = f"""
        Name: {name}
        Email: {email}
        Phone: {number}
        Subject: {subject}

        Message:
        {message}
        """

        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = EMAIL_ADDRESS

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()

        flash("Message sent successfully!")

    except Exception as e:
        print(e)
        flash("Error sending message!")

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)