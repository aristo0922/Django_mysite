from django.shortcuts import render

# Create your views here.
def hello_world(request):

    if request.method=="POST":
        return render(request, 'account/hello_world.html', context={'text':'POST METHOD!!'})
    else:
            return render(request, 'account/hello_world.html', context={'text':'GET!!'})

