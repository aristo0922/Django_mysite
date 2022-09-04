from django.shortcuts import render

# Create your views here.
def hello_world(request):

    if request.method=="POST":
        temp = request.POST.get('hello_world_input')
        return render(request, 'account/hello_world.html', context={'text':temp})
    else:
            return render(request, 'account/hello_world.html', context={'text':'GET!!'})

