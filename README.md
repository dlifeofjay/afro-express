# 📧 Email Campaign for General Event Attendees (email_AT.py)

A Python script for sending promotional emails to general event attendees who haven't been segmented into behavioral clusters.

## 🎯 Purpose

This script sends a standardized promotional email to all remaining attendees from the `remaining_attendees.csv` file. Unlike `testemail.py` which uses cluster-based personalization, this script sends the same message to everyone.

## 📂 Project Structure

```
afro-express-campaign/
│
├── testemail.py              # Cluster-based campaign (segmented attendees)
├── email_AT.py               # This file - General attendees campaign
├── email_attendees.csv       # Clustered attendees data
├── remaining_attendees.csv   # General attendees data
└── README.md                 # Documentation
```

## 🔄 Relationship to testemail.py

| Feature | testemail.py | email_AT.py |
|---------|--------------|-------------|
| **Target Audience** | Segmented customers (Clusters 0, 1, 2) | General attendees (no clustering) |
| **Data File** | `email_attendees.csv` | `remaining_attendees.csv` |
| **Personalization** | 3 different messages by cluster | 1 standard message for all |
| **Use Case** | High-value, repeat customers | New or unclassified attendees |

## ✨ Features

- **Batch Processing**: Sends 50 emails at a time with breaks
- **Rate Limiting**: 12-second delays between emails to avoid spam flags
- **Duplicate Prevention**: Automatically removes duplicate email addresses
- **Row Selection**: Configurable start/end rows for controlled sending
- **Progress Tracking**: Real-time delivery status updates
- **Error Handling**: Continues sending even if some emails fail
- **HTML Support**: Rich, visually appealing email format

## 📋 Prerequisites

### Required Python Libraries
```bash
pip install pandas
```

### Gmail Setup
1. Enable **2-Factor Authentication** on your Gmail account
2. Generate an **App Password**:
   - Go to Google Account → Security → 2-Step Verification → App Passwords
   - Create a new app password for "Mail"
   - Copy the 16-character password

### Required Files
- `remaining_attendees.csv` - Must contain these columns:
  - `Buyer email` - Recipient email address
  - `Buyer first name` - Recipient's first name

## 🚀 Quick Start

1. **Update credentials** in the script:
   ```python
   SENDER_EMAIL = "your-email@gmail.com"
   SENDER_PASSWORD = "your-app-password"
   ```

2. **Configure row range** (optional):
   ```python
   df = df.iloc[606:640]  # Adjust start:end rows
   ```

3. **Run the script**:
   ```bash
   python email_AT.py
   ```

## ⚙️ Configuration

### Row Selection Options

```python
# Send to ALL remaining attendees
df = df.iloc[:]

# Send to first 250 rows
df = df.iloc[:250]

# Send rows 251-450
df = df.iloc[250:450]

# Send rows 606-640 (as currently configured)
df = df.iloc[606:640]
```

### Batch Settings

```python
BATCH_SIZE = 50        # Emails per batch
BATCH_DELAY = 300      # Seconds between batches (5 minutes)
EMAIL_DELAY = 12       # Seconds between individual emails
```

### Email Content

To modify the email, edit the `get_email_content()` function:
```python
def get_email_content(first_name):
    subject = "Your subject here"
    body = """Your HTML content here"""
    return subject, body
```

## 📧 Email Template

The script sends a single standardized message:

- **Subject**: "🎟️ LAST CALL — Lock in Your Ticket for Cash Cobain X DJ Tunez at AfroTech!"
- **Content**: 
  - Personalized greeting using first name
  - Event details (date, time, location)
  - Featured artists (Cash Cobain & DJ Tunez)
  - Call-to-action button for ticket purchase
  - Event flyer image

## 🛡️ Safety Guidelines

### Daily Sending Limits
- **Gmail Regular Account**: 500 emails/day max
- **Recommended**: 200-250 emails per day for safety
- **First Campaign**: Start with 100-150 emails

### Multi-Day Campaign Strategy

For 640 remaining attendees:
```
Day 1: Rows 0-200     (200 emails)
Day 2: Rows 200-400   (200 emails)
Day 3: Rows 400-600   (200 emails)
Day 4: Rows 600-640   (40 emails)
```

Update the row range each day:
```python
# Day 1
df = df.iloc[0:200]

# Day 2
df = df.iloc[200:400]

# Day 3
df = df.iloc[400:600]

# Day 4
df = df.iloc[600:640]
```

## 📊 Campaign Timeline

For current configuration (rows 606-640 = 34 emails):
- **Duration**: ~7 minutes
- **Calculation**: 34 emails × 12 seconds = 408 seconds (~7 min)

For a full 200-email batch:
- **Duration**: ~45-50 minutes
- **Includes**: Batch delays between every 50 emails

## 📝 Example CSV Format

```csv
Buyer email,Buyer first name
john.doe@example.com,John
jane.smith@example.com,Jane
alex.jones@example.com,Alex
sarah.wilson@example.com,
```
*Note: Missing first names will default to "there"*

## 🔍 Monitoring Output

```
📧 Preparing to send 34 emails...

🚀 Starting Batch 1 (34 emails)...
✅ [1/34] Sent to john.doe@example.com
✅ [2/34] Sent to jane.smith@example.com
❌ Failed for invalid@email.com: [Error message]

==================================================
🎯 Email Campaign Complete!
📧 Total sent: 33
❌ Failed: 1
⏱️  Duration: 0:06:48
==================================================
```

## 🐛 Troubleshooting

### "Authentication failed"
- Verify app password is correct
- Ensure 2FA is enabled

### "Daily sending limit exceeded"
- Wait 24 hours
- Reduce batch size or split across more days

### Emails going to spam
- Reduce sending rate (increase `EMAIL_DELAY`)
- Add unsubscribe link
- Warm up account with smaller batches

### "Connection timeout"
- Check internet connection
- Verify firewall settings (port 465)

## 🔐 Security Best Practices

1. **Never commit credentials** to GitHub/Git
2. **Use environment variables**:
   ```python
   import os
   SENDER_PASSWORD = os.getenv('EMAIL_APP_PASSWORD')
   ```
3. **Add to .gitignore**:
   ```
   remaining_attendees.csv
   *.env
   config.py
   ```

## 📈 Campaign Workflow

### Complete Multi-File Campaign Strategy

1. **Day 1**: Run `testemail.py` (250 segmented customers)
   - Target: High-value clusters
   - Personalized messaging
   
2. **Day 2**: Run `email_AT.py` rows 0-200 (200 general attendees)
   - Standard promotional message
   
3. **Day 3**: Run `email_AT.py` rows 200-400 (200 more attendees)

4. **Day 4**: Run `email_AT.py` rows 400-640 (remaining attendees)

### Why This Approach?
- **Prioritizes high-value customers** (clustered data first)
- **Stays within Gmail limits** (200-250/day)
- **Reduces spam risk** (gradual sending)
- **Maximizes deliverability** (warm sending pattern)

## 🆚 When to Use Each Script

| Scenario | Use Script | Reason |
|----------|-----------|---------|
| Past buyers with purchase history | `testemail.py` | Cluster-based targeting |
| New attendees | `email_AT.py` | No behavioral data yet |
| General promotion | `email_AT.py` | Same message for all |
| VIP/Repeat customers | `testemail.py` | Personalized approach |

## 📚 Advanced Customization

### Adding Tracking Parameters
```python
ticket_link = "https://posh.vip/e/event?utm_source=email&utm_campaign=lastcall"
```

### Multiple Message Variants
Modify the function to A/B test:
```python
def get_email_content(first_name, variant='A'):
    if variant == 'A':
        subject = "Version A subject"
    else:
        subject = "Version B subject"
    # ...
```

### Unsubscribe Link
```python
body = f"""
{your_content}
<hr>
<p style="font-size:10px;color:#666;">
Don't want these emails? 
<a href="https://your-unsubscribe-link.com">Unsubscribe</a>
</p>
"""
```

## 📊 Results Tracking

After campaign completion, monitor:
- ✅ Delivery success rate
- ❌ Failed sends (and why)
- 📈 Ticket sales (check Posh.vip analytics)
- 📧 Open rates (requires tracking pixels)
- 🎯 Click-through rates (UTM parameters)

## 🤝 Support

For issues:
1. Check Gmail SMTP settings
2. Verify CSV format
3. Review error messages in output
4. Test with 5-10 emails first

---

**Part of Afro-Express Email Campaign System** 🎉
- `testemail.py` → Segmented customers
- `email_AT.py` → General attendees (this file)