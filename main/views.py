from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
    return render(request, 'main/home.html')

def contact(request):
    if request.method == 'POST':
        if request.POST.get('email', False):
            name = request.POST['name']
            email = request.POST['email']
            subject = request.POST['subject']
            number = request.POST['number']
            message = request.POST['message']

            message += '\n\n' + name + '\n' + email + '\n' + number
            subject += ' /**\ ' + name + ' /**\ ' + email + '/**\ ' + number

            send_mail(
                subject,
                message,
                'pa.ko.doradca@gmail.com',
                ['pa.ko.doradca@gmail.com'],
                fail_silently=False
            )

    return render(request, 'main/contact.html')

def blog(request):
    return render(request, 'main/blog.html')