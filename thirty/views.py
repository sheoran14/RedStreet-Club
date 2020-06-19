from django.shortcuts import render

# Create your views here.


def thirty(request):

    return render(request, 'home.html', {})
