import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time


# STEP 1: Load your dataset

# Must include columns: Email, FirstName, Cluster
df = pd.read_csv("email_attendees.csv")

# Clean duplicates so one email per person
df = df.drop_duplicates(subset='Buyer email', keep='first')


# STEP 2: Define sender info

SENDER_EMAIL = "afroexpressatx@gmail.com"
SENDER_PASSWORD = "akqtskokwfcokskc"


# STEP 3: Define email templates

def get_email_content(cluster, first_name):
    first_name = first_name if pd.notna(first_name) else "there"
    image_url = "https://drive.google.com/uc?export=view&id=13iLVeNtVURsyNA0acqHfvCw9nCe08cNK"   # Replace with your flyer image URL
    ticket_link = "https://posh.vip/e/night-in-motion-cash-cobain-x-dj-tunez-in-houston"

    
    # Cluster 0 — Average one-ticket buyers
    
    if cluster == 0:
        subject = "🎟️ LAST CALL — Lock in Your Ticket for Cash Cobain X DJ Tunez at AfroTech!"
        body = f"""
        <html><body>
        <p>Hey {first_name},</p>
        <center>
          <img src="{image_url}" alt="AfroTech in Houston"
          style="width:100%;max-width:600px;border-radius:12px;margin-bottom:20px;">
        </center>
        <p>We noticed you’ve been part of the vibe before, and Afro-Express is back — bigger and better! 🔥</p>
        <p>This Thursday at <b>3333 Raleigh St, Houston, TX 77021 Starting 7PM Central Time</b>, we’re bringing the ultimate Afro-fusion experience with <b>Cash Cobain</b> & <b>DJ Tunez</b>.</p>
        <p>Lock in your ticket now before prices rise or it sells out.</p>
        <p><a href="{ticket_link}" style="color:#E63946;font-weight:bold;">🎟️ Get Your Ticket →</a></p>
        <p>See you at The Address!<br><b>– The Afro-Express Team</b></p>
        </body></html>
        """

    
    # Cluster 1 — Early proactive buyers
    
    elif cluster == 1:
        subject = "🎟️ LAST CALL — Lock in Your Ticket for Cash Cobain X DJ Tunez at AfroTech!"
        body = f"""
        <html><body>
        <p>Hey {first_name},</p>
        <center>
          <img src="{image_url}" alt="AfroTech in Houston"
          style="width:100%;max-width:600px;border-radius:12px;margin-bottom:20px;">
        </center>
        <p>The countdown is on — <b>Afro-Express</b> returns to <b>3333 Raleigh St, Houston, TX 77021 Starting 7PM Central Time</b> this Thursday 30th October! 💃🏾🕺🏾</p>
        <p>You’ve supported us before, and we’d love to see you again as we turn up the energy for this special edition featuring <b>Cash Cobain</b> & <b>DJ Tunez</b>.</p>
        <p>Don’t wait till the last minute — tickets are almost gone.</p>
        <p><a href="{ticket_link}" style="color:#E63946;font-weight:bold;">🎟️ Grab Your Ticket Now →</a></p>
        <p>Let’s make Thursday unforgettable.<br><b>– The Afro-Express Team</b></p>
        </body></html>
        """

    
    # Cluster 2 — Group / high-value buyers
    
    elif cluster == 2:
        subject = "🎟️ LAST CALL — Lock in Your Ticket for Cash Cobain X DJ Tunez at AfroTech!"
        body = f"""
        <html><body>
        <p>Hey {first_name},</p>
        <center>
          <img src="{image_url}" alt="Afro-Express Houston"
          style="width:100%;max-width:600px;border-radius:12px;margin-bottom:20px;">
        </center>
        <p>You and your crew know how to bring the energy 💥</p>
        <p><b>Afro-Express</b> is happening this Thursday 30th October at <b>3333 Raleigh St, Houston, TX 77021 Starting 7PM Central Time</b>, featuring <b>Cash Cobain</b> and <b>DJ Tunez</b> — an all-night Afro-fusion experience you don’t want to miss.</p>
        <p>Group tickets are almost gone — get yours now and pull up with your people.</p>
        <p><a href="{ticket_link}" style="color:#E63946;font-weight:bold;">🎟️ Reserve Your Group’s Spot →</a></p>
        <p>It’s about to be a movie!<br><b>– The Afro-Express Team</b></p>
        </body></html>
        """

    
    # Default (fallback)
    
    else:
        subject = "Afro-Express Is Almost Here!"
        body = f"""
        <html><body>
        <p>Hey {first_name},</p>
        <center>
          <img src="{image_url}" alt="Afro-Express Houston"
          style="width:100%;max-width:600px;border-radius:12px;margin-bottom:20px;">
        </center>
        <p>The countdown is on — <b>Afro-Express</b> is happening this Thursday 30th October at <b>3333 Raleigh St, Houston, TX 77021 Starting 7PM Central Time</b>.</p>
        <p><a href="{ticket_link}" style="color:#E63946;font-weight:bold;">🎟️ Grab Your Ticket →</a></p>
        <p>See you soon!<br><b>– The Afro-Express Team</b></p>
        </body></html>
        """

    return subject, body


# STEP 4: Email sending function

def send_email(to_email, subject, body):
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
        print(f"✅ Sent to {to_email}")
    except Exception as e:
        print(f"❌ Failed for {to_email}: {e}")


# STEP 5: Loop through and send

for _, row in df.iterrows():
    email = row['Buyer email']
    cluster = row['labels']
    first_name = row['Buyer first name']

    subject, body = get_email_content(cluster, first_name)
    send_email(email, subject, body)
    time.sleep(10)  # Delay between sends to reduce spam flag risk

print("🎯 All emails sent successfully!")