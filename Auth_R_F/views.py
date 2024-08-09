from django.shortcuts import render, redirect
import logging
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from .models import *
from django.urls import reverse
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils import timezone

logger = logging.getLogger(__name__)

@login_required
def Home(request):
    return render(request, "Auth_R_F/index.html")

def RegisterView(request):
    if request.method == 'POST':
        # getting user inputs from frontend
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_data_has_error = False

        if User.objects.filter(username=username).exists():
            user_data_has_error = True
            messages.error(request, _('Username already exists'))

        if User.objects.filter(email=email).exists():
            user_data_has_error = True
            messages.error(request, _('Email already exists'))

        if len(password) < 4:
            user_data_has_error = True
            messages.error(request, _('Password must be at least 8 characters long'))

        if user_data_has_error:
            context = {
                'first_name': first_name,
                'last_name': last_name,
                'username': username,
                'email': email,
                'password': password
            }
            return render(request, 'Auth_R_F/register.html', context)
        if not user_data_has_error:
            new_user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password
            )
            messages.success(request, _("Account created. Login now"))

            new_user.save()
            
            return redirect('Auth_R_F:login')
    return render(request, 'Auth_R_F/register.html')


def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        logger.info("Attempting to log in user: %s", username)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, _("Logged in successfully"))
                logger.info("User logged in successfully: %s", username)
                return redirect('Auth_R_F:home')
            else:
                messages.error(request, _("Your account is inactive"))
                logger.warning("Inactive account: %s", username)
        else:
            messages.error(request, _("Invalid login credentials"))
            logger.warning("Invalid login attempt: %s", username)
        return redirect('Auth_R_F:login')
    return render(request, "Auth_R_F/login.html")



def LogoutView(request):
    logout(request)
    return redirect('Auth_R_F:login')


def ForgotPassword(request):

    if request.method == 'POST':
        email = request.POST.get('email')

        try:
            user = User.objects.get(email=email)

            new_password_reset = PasswordReset(user=user)
            new_password_reset.save()

            
            password_reset_url = reverse('Auth_R_F:reset-password', kwargs={'reset_id': new_password_reset.reset_id})

            full_password_reset_url = f'{request.scheme}://{request.get_host()}{password_reset_url}'

            email_body = f'Reset your password using the link below:\n\n\n{full_password_reset_url}'

            email_message = EmailMessage(
                'Reset your password', # email subject
                email_body,
                settings.EMAIL_HOST_USER, # email sender
                [email] # email  receiver 
            )

            email_message.fail_silently = True
            email_message.send()

            return redirect('Auth_R_F:password-reset-sent', reset_id=new_password_reset.reset_id)

        except User.DoesNotExist:

            messages.error(request, _('User does not exist'))
            messages.info(request, email)

            return redirect('Auth_R_F:forgot-password')

    return render(request, 'Auth_R_F/forgot_password.html')


def PasswordResetSent(request, reset_id):

    if PasswordReset.objects.filter(reset_id=reset_id).exists():
        return render(request, 'Auth_R_F/password_reset_sent.html')
    else:
        # redirect to forgot password page if code does not exist
        messages.error(request, 'Invalid reset id')
        return redirect('forgot-password')

def ResetPassword(request, reset_id):

    try:
        password_reset_id = PasswordReset.objects.get(reset_id=reset_id)

        if request.method == "POST":
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            passwords_have_error = False

            if password != confirm_password:
                passwords_have_error = True
                messages.error(request, 'Passwords do not match')

            if len(password) < 5:
                passwords_have_error = True
                messages.error(request, 'Password must be at least 5 characters long')

            expiration_time = password_reset_id.created_when + timezone.timedelta(minutes=10)

            if timezone.now() > expiration_time:
                passwords_have_error = True
                messages.error(request, 'Reset link has expired')

                password_reset_id.delete()

            if not passwords_have_error:
                user = password_reset_id.user
                user.set_password(password)
                user.save()

                password_reset_id.delete()

                messages.success(request, 'Password reset. Proceed to login')
                return redirect('Auth_R_F:login')
            else:
                # redirect back to password reset page and display errors
                return redirect('Auth_R_F:reset-password', reset_id=reset_id)

    
    except PasswordReset.DoesNotExist:
        
        # redirect to forgot password page if code does not exist
        messages.error(request, 'Invalid reset id')
        return redirect('Auth_R_F:forgot-password')

    return render(request, 'Auth_R_F/reset_password.html')