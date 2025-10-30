import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from datetime import datetime

# STEP 1: Load your dataset and start from row 251
df = pd.read_csv("remaining_attendees.csv")
df = df.drop_duplicates(subset='Buyer email', keep='first')

# START FROM ROW 251 TO THE END
df = df.iloc[606:640]  # just the 400 for today
print(f"📧 Preparing to send {len(df)} emails...")

# STEP 2: Define sender info
SENDER_EMAIL = "afroexpressatx@gmail.com"
SENDER_PASSWORD = "akqtskokwfcokskc"

# Safety settings
BATCH_SIZE = 50  # Send in batches
BATCH_DELAY = 300  # 5 minutes between batches (in seconds)
EMAIL_DELAY = 12  # 12 seconds between individual emails

# STEP 3: Define email template
def get_email_content(first_name):
    """Return subject and body for each recipient."""
    first_name = first_name if pd.notna(first_name) else "there"
    image_url = "https://drive.google.com/uc?export=view&id=13iLVeNtVURsyNA0acqHfvCw9nCe08cNK"
    ticket_link = "https://posh.vip/e/night-in-motion-cash-cobain-x-dj-tunez-in-houston"

    subject = "🎟️ LAST CALL — Lock in Your Ticket for Cash Cobain X DJ Tunez at AfroTech!"
    body = f"""
    <html><body>
    <p>Hey {first_name},</p>
    <center>
      <img src="{image_url}" alt="AfroTech in Houston"
      style="width:100%;max-width:600px;border-radius:12px;margin-bottom:20px;">
    </center>
    <p>We noticed you've been part of the vibe before, and Afro-Express is back — bigger and better! 🔥</p>
    <p>This Thursday at <b>3333 Raleigh St, Houston, TX 77021 Starting 7PM Central Time</b>, we're bringing the ultimate Afro-fusion experience with <b>Cash Cobain</b> & <b>DJ Tunez</b>.</p>
    <p>Lock in your ticket now before prices rise or it sells out.</p>
    <p><a href="{ticket_link}" style="color:#E63946;font-weight:bold;">🎟️ Get Your Ticket →</a></p>
    <p>See you at The Address!<br><b>– The Afro-Express Team</b></p>
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
        return True
    except Exception as e:
        print(f"❌ Failed for {to_email}: {e}")
        return False

# STEP 5: Send in batches with delays
total_sent = 0
total_failed = 0
start_time = datetime.now()

for batch_num in range(0, len(df), BATCH_SIZE):
    batch_df = df.iloc[batch_num:batch_num + BATCH_SIZE]
    batch_count = batch_num // BATCH_SIZE + 1
    
    print(f"\n🚀 Starting Batch {batch_count} ({len(batch_df)} emails)...")
    
    for idx, row in batch_df.iterrows():
        email = row['Buyer email']
        first_name = row['Buyer first name']

        subject, body = get_email_content(first_name)
        
        if send_email(email, subject, body):
            total_sent += 1
            print(f"✅ [{total_sent}/{len(df)}] Sent to {email}")
        else:
            total_failed += 1
        
        # Delay between individual emails
        time.sleep(EMAIL_DELAY)
    
    # Delay between batches (except after the last batch)
    if batch_num + BATCH_SIZE < len(df):
        print(f"⏸️  Pausing for {BATCH_DELAY//60} minutes before next batch...")
        time.sleep(BATCH_DELAY)

end_time = datetime.now()
duration = end_time - start_time

print(f"\n{'='*50}")
print(f"🎯 Email Campaign Complete!")
print(f"📧 Total sent: {total_sent}")
print(f"❌ Failed: {total_failed}")
print(f"⏱️  Duration: {duration}")
print(f"{'='*50}")
