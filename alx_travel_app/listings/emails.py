from django.core.mail import send_mail
from django.conf import settings

def send_payment_confirmation_email(email, booking_id, amount):
    """
    Send a payment confirmation email for successfully Chapa payment.
    """

    subject = "Payment Successful - Booking Confirmed"

    message = (
        f"""
        Hello,
        Your payment was successful 🎉
        Amount Paid: {amount}
        Your booking has been confirmed.
        Thank you for choosing our travel service.
        Best regards, Travel Booking Team.
        """
    )

    send_mail(
        subject=subject,
        message=message,
        from_email=setting.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
        fail_silently=False
    )
