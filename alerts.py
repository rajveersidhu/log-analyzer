import smtplib
from email.mime.text import MIMEText
from parser import parse_logs

# Configuration
SENDER_EMAIL = "your-email@example.com"
SENDER_PASSWORD = "your-password"
RECIPIENT_EMAIL = "admin@example.com"

def send_alert(ip_address, username, log_entry):
    subject = "🚨 Suspicious Login Attempt Detected!"
    body = f"""
    Suspicious Login Attempt Detected:
    - User: {username}
    - IP Address: {ip_address}
    - Log Entry: {log_entry}
    """

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECIPIENT_EMAIL

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())

    print("🚀 Alert Sent Successfully!")

if __name__ == "__main__":
    logs = parse_logs()
    if logs:
        for entry in logs:
            send_alert(entry[1], entry[0], entry[2])
