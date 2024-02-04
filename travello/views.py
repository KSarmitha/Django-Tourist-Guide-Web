from django.http import HttpResponse
from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):
    # return HttpResponse("Hello World!")
    # dest1 = Destination()
    # dest1.name = 'Sri Lanka'
    # dest1.desc = 'The most beautiful place in the world'
    # dest1.img = 'destination_1.jpg'
    # dest1.price = 1500
    # dest1.offer = True

    # dest2 = Destination()
    # dest2.name = 'India'
    # dest2.desc = "The world's most populous democracy"
    # dest2.img = 'destination_4.jpg'
    # dest2.price = 1000
    # dest2.offer = True

    # dest3 = Destination()
    # dest3.name = 'France'
    # dest3.desc = 'The most next beautiful place in the world'
    # dest3.img = 'destination_6.jpg'
    # dest3.price = 2000
    # dest3.offer = False

    # destination = [dest1, dest2, dest3]

    destination = Destination.objects.all()
    return render(request, 'index.html', {'destination': destination})