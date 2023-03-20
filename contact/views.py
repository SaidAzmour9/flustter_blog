from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Info
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def send_message(request):
      myinfo = Info.objects.first()
      if request.method == 'POST':
               message = request.POST['message']
               name = request.POST['name']
               email = request.POST['email']
               subject = request.POST['subject']
      Context ={'myinfo':myinfo}
      """send_mail(subject= subject,message= message,from_email=settings.DEFAULT_FROM_EMAIL,recipient_list = [email],fail_silently  = True,)
      return redirect('fooview')"""

      Context = {}

      return render(request, 'contact/contact.html', Context)