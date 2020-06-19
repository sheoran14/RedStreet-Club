from django.shortcuts import render, redirect
from tournament.models import Contact
from tournament.models import Power
from tournament.models import Body
from tournament.models import Badminton
from tournament.models import Ttennis
from tournament.models import Chess
from .forms import MakeForm
#from .models import Parti
from django.http import HttpResponse

# Create your views here.



def tournament(request):

    return render(request, 'det.html', {})
def pwl(request):

    return render(request, 'det.html', {})
def bbl(request):

    return render(request, 'det.html', {})
def minton(request):

    return render(request, 'det.html', {})
def tennis(request):

    return render(request, 'det.html', {})
def che(request):
    return render(request, 'det.html', {})
def arm(request):
    cont = Contact.objects.all()
    return render(request, 'arm.html', {'cont': cont})
def plift(request):
    obj = Power.objects.all()
    return render(request, 'powlift.html', {'obj': obj})
def bmint(request):
    sbj = Badminton.objects.all()
    return render(request, 'minton.html', {'sbj': sbj})
def bbild(request):
    fbj = Body.objects.all()
    return render(request, 'bodybuild.html', {'fbj': fbj})
def ten(request):
    tbj = Ttennis.objects.all()
    return render(request, 'tt.html', {'tbj': tbj})
def king(request):
    kq = Chess.objects.all()
    return render(request, 'ces.html', {'kq': kq})
#def ChessFn(request):
    #obj = Chess.objects.all()
    #return render(request, 'tournament.html', {'obj': obj})

def new(request):
    return render(request, 'check.html', {})
def pay(request):
    form = MakeForm(request.POST)
    if request.method == 'POST':

        if form.is_valid():
          form.save()
          form = MakeForm()
    return render(request, 'payment.html', {'form': form})



#def ooo(request):
    #game = Parti.objects.all()
    #return render(request, 'profile.html', {'game': game})
