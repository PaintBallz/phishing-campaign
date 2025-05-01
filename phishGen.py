import torch
from transformers import pipeline
import smtplib
from email.message import EmailMessage

def load_gpt_model():
    device = 0 if torch.cuda.is_available() else -1
    generator = pipeline("text-generation", model="openai-community/gpt2-medium", device=device)
    return generator 

def generate_email_template(generator, company_name, max_length=300):
    prompt = f"""
    You are a skilled email communication artifical intelligence agent with extensive experience in crafting professional and empathetic messages for various situations to be communicated over electronic mail. Your expertise lies in ensuring that sensitive communications are clear, reassuring, and actionable.
    Your task is to generate an email body for notifying users about a password reset due to a recent breach of the company's password database that has since been resolved.
    The email should include a clear explanation of the situation, instructions for resetting the password via a button link, and an emphasis on the importance of maintaining account security.
    Please keep in mind the following details:
    Company Name: {company_name}
    Brief explanation of the breach: the breach occured last week but has been resolved
    Instructions for resetting the password: press the link to have your password reset
    """

    generated_text = generator(
        prompt,
        max_length=max_length,
        num_return_sequences=1,
        temperature=0.9,     # 0.7
        top_k=70,            # 50
        top_p=0.9            # 0.9
    )[0]['generated_text']

    if generated_text.startswith(prompt):
        generated_text = generated_text[len(prompt):].strip()

    return generated_text.strip()

button_link = "MALICIOUS_LINK"

def format_email_as_html(email_text, company_name):
    return f"""
    <html>
    <body style="font-family: Arial, sans-serif; line-height: 1.6;">
        <p>Dear User,</p>
        <p>{email_text}</p>
        <p><a href="{button_link}" 
              style="display: inline-block; background-color: #007bff; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">
              Reset Password
           </a>
        </p>
        <p>If you didn’t request this, please contact our security team immediately.</p>
        <p>Best regards,<br><strong>{company_name} Security Team</strong></p>
    </body>
    </html>
    """

def send_email(subject, html_content, to_email, from_email, mailjet_api_key, mailjet_secret_key):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    msg.set_content("This email requires an HTML-capable email client.")
    msg.add_alternative(html_content, subtype='html')

    try:
        with smtplib.SMTP('in-v3.mailjet.com', 587) as smtp:
            smtp.starttls()
            smtp.login(mailjet_api_key, mailjet_secret_key)
            smtp.send_message(msg)
        print("Email sent successfully.")
    except Exception as e:
        print("Error sending email:", e)

if __name__ == "__main__":
    generator = load_gpt_model()
    company_name = "ADP"
    email_text = generate_email_template(generator, company_name)
    email_template = format_email_as_html(email_text, company_name)

    mailjet_api_key = "MAILJET_API_KEY"
    mailjet_secret_key = "MAILJET_SECRET_KEY"

    from_email = "SENDER_EMAIL"
    to_email = "VICTIM_EMAIL"

    send_email(
        subject=f"{company_name} - Password Reset Notification",
        html_content = email_template,
        to_email = to_email,
        from_email = from_email,
        mailjet_api_key = mailjet_api_key,
        mailjet_secret_key = mailjet_secret_key
    )