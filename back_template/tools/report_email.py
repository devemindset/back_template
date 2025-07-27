from django.core.mail import EmailMultiAlternatives
from django.conf import settings

DEFAULT_FROM_EMAIL= settings.DEFAULT_FROM_EMAIL
CONTACT_RECEIVER_EMAIL= settings.CONTACT_RECEIVER_EMAIL

def welcome_notification_email(receiver_email):
    subject = "Welcome to TimeTallyApp ⏱️"
    from_email = DEFAULT_FROM_EMAIL
    to = [receiver_email]
    text_content = "Welcome to TimeTallyApp!"

    html_content = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Welcome to TimeTallyApp</title>
</head>
<body style="font-family: 'Segoe UI', Tahoma, sans-serif; background-color: #f5f7fb; padding: 30px; color: #333;">
  <table width="100%" cellspacing="0" cellpadding="0" style="max-width: 600px; margin: auto; background-color: white; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.05); overflow: hidden;">
    <tr>
      <td style="padding: 30px;">
        <h1 style="color: #2c3e50; font-size: 26px; margin-bottom: 10px;">⏱️ Welcome to TimeTallyApp</h1>
        <p style="font-size: 16px; line-height: 1.5; margin-bottom: 20px;">
          We're glad to have you! TimeTallyApp helps you track your work time easily and generate beautiful reports that impress your clients or team.
        </p>
        <p style="font-size: 16px; line-height: 1.5; margin-bottom: 20px;">
          Whether you're working solo or managing multiple projects, TimeTallyApp lets you stay organized and focused — without wasting time on spreadsheets or clunky tools.
        </p>
        <p style="font-size: 16px; line-height: 1.5; margin-bottom: 20px;">
          Get started by creating your first project, adding sessions, and generating your first report in just a few clicks.
        </p>
        <p style="font-size: 14px; color: #777; margin-top: 40px;">
          This is an automated message. Please do not reply.
        </p>
        <p style="font-size: 16px; margin-top: 10px;">– The TimeTallyApp Team</p>
      </td>
    </tr>
  </table>
</body>
</html>
"""

    msg = EmailMultiAlternatives(
        subject,
        text_content,
        from_email,
        to,
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()
def forward_contact_message(user_email, user_message):
    """
    Transfère un message de contact vers ton adresse support avec version HTML.
    """
    subject = f"📩 Nouveau message de {user_email}"
    from_email = DEFAULT_FROM_EMAIL
    to = ["gogmongoma@gmail.com"]

    # ✅ Version texte brut (fallback)
    text_content = f"""
    Nouveau message de contact :

  
    Email : {user_email}

    Message :
    {user_message}
    """

    # ✅ Version HTML stylisée
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <body style="font-family: Arial, sans-serif; line-height: 1.6;">
        <h2>📩 Nouveau message de contact</h2>
        <p><strong>Email :</strong> {user_email}</p>
        <p><strong>Message :</strong></p>
        <p style="background:#f5f5f5;padding:10px;border-left:4px solid #00bfff;">{user_message}</p>
        <hr>
        <p>Ce message provient du formulaire de contact de timetallyapp.</p>
    </body>
    </html>
    """

    msg = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        from_email=from_email,
        to=to,
        reply_to=[user_email],  # ✅ Ici tu pourras répondre directement au visiteur
    )

    msg.attach_alternative(html_content, "text/html")
    msg.send()



def send_verification_email(email, code):
    subject = "Verify your TimeTally account"
    from_email = settings.DEFAULT_FROM_EMAIL
    to = [email]
    text_content = f"Your verification code is: {code}"

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8">
      <title>Email Verification</title>
    </head>
    <body style="font-family: 'Segoe UI', Tahoma, sans-serif; background-color: #f5f7fb; padding: 30px; color: #333;">
      <table width="100%" cellspacing="0" cellpadding="0" style="max-width: 600px; margin: auto; background-color: white; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.05); overflow: hidden;">
        <tr>
          <td style="padding: 30px;">
            <h1 style="color: #2c3e50; font-size: 26px; margin-bottom: 10px;">🔐 Verify your Email</h1>
            <p style="font-size: 16px; line-height: 1.5; margin-bottom: 20px;">
              You're almost there! Use the verification code below to activate your TimeTally account.
            </p>
            <div style="font-size: 32px; font-weight: bold; background-color: #eef2ff; color: #4f46e5; padding: 15px 25px; border-radius: 8px; text-align: center; letter-spacing: 4px;">
              {code}
            </div>
            <p style="font-size: 16px; line-height: 1.5; margin-top: 20px;">
              This code will expire in 15 minutes.
            </p>
            <p style="font-size: 14px; color: #777; margin-top: 40px;">
              This is an automated email. Please do not reply.
            </p>
            <p style="font-size: 16px; margin-top: 10px;">– The TimeTally Team</p>
          </td>
        </tr>
      </table>
    </body>
    </html>
    """

    msg = EmailMultiAlternatives(
        subject,
        text_content,
        from_email,
        to,
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()

def website_action_message(type, place):
    """
    .
    """
    subject = f"📩 Nouveau message de {type}"
    from_email = DEFAULT_FROM_EMAIL
    to = ["gogmongoma@gmail.com"]

    # ✅ Version texte brut (fallback)
    text_content = f"""
    Nouveau message de {type} :

  
    

    Message :
    {place}
    """

    # ✅ Version HTML stylisée
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <body style="font-family: Arial, sans-serif; line-height: 1.6;">
        <h2>📩 Nouveau {type} contact</h2>
   
        <p><strong>Message :</strong></p>
        <p style="background:#f5f5f5;padding:10px;border-left:4px solid #00bfff;">{place}</p>
        <hr>
        <p>nouveau {type} timetallyapp.</p>
    </body>
    </html>
    """

    msg = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        from_email=from_email,
        to=to,
        # reply_to=[user_email],  # ✅ Ici tu pourras répondre directement au visiteur
    )

    msg.attach_alternative(html_content, "text/html")
    msg.send()

def send_payment_confirmation_email(email, amount):
    subject = "Your Payment Confirmation – TimeTally"
    from_email = settings.DEFAULT_FROM_EMAIL
    to = [email]

    text_content = f"Thank you for your payment of ${amount:.2f}. Your transaction has been successfully processed."

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8">
      <title>Payment Confirmation</title>
    </head>
    <body style="font-family: 'Segoe UI', Tahoma, sans-serif; background-color: #f5f7fb; padding: 30px; color: #333;">
      <table width="100%" cellspacing="0" cellpadding="0" style="max-width: 600px; margin: auto; background-color: white; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.05); overflow: hidden;">
        <tr>
          <td style="padding: 30px;">
            <h1 style="color: #2c3e50; font-size: 24px; margin-bottom: 10px;">💳 Payment Confirmation</h1>
            <p style="font-size: 16px; line-height: 1.5; margin-bottom: 20px;">
              Thank you for your payment! We’ve successfully processed your transaction.
            </p>
            <div style="font-size: 28px; font-weight: bold; background-color: #ecfdf5; color: #059669; padding: 15px 25px; border-radius: 8px; text-align: center;">
              ${amount:.2f}
            </div>
            <p style="font-size: 16px; line-height: 1.5; margin-top: 20px;">
              You can now enjoy all the features included with your plan.
            </p>
            <p style="font-size: 14px; color: #777; margin-top: 40px;">
              This is an automated email. Please do not reply.
            </p>
            <p style="font-size: 16px; margin-top: 10px;">– The TimeTally Team</p>
          </td>
        </tr>
      </table>
    </body>
    </html>
    """

    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()