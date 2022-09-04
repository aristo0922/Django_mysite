from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from account.models import user


def hello_world(request):

    if request.method=="POST":
        input_name = request.POST.get('user_name')
        input_email = request.POST.get('user_email')
        input_password = request.POST.get('user_password')

        new_user=user(name=input_name, email=input_email, password=input_password, is_deleted=False)
        new_user.save()

        return HttpResponseRedirect(reverse('account:hello_world'))
    else:
        new_user_list = user.objects.all()
        return render(request, 'account/hello_world.html', context={'new_user_list':new_user_list})

