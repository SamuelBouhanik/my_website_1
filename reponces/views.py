from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from django.core.mail import send_mail

def see_reponces(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            reponces = request.POST['reponces']
            send_mail(
                f'Reponse de {request.user.username}',
                f'{reponces}',
                'Django.get.1@gmail.com',
                ['Django.get.1@gmail.com'],
                fail_silently=False,
            )
    else:
        messages.error(request, 'You need to register first before go to RSVP')
        return render(request, 'accounts/register.html')


    return render(request,'Reponces/reponces.html')
