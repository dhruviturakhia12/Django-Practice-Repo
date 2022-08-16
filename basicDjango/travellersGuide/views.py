from django.shortcuts import render
from .models import Destination
# from django.shortcuts import HttpResponse
def index(request):
    # dest1 = Destination()
    # dest1.img = "destination_1.jpg"
    # dest1.name = "Mumbai"
    # dest1.desc = "City never sleeps"
    # dest1.price = "From $ 450"
    # dest1.offer = False
    #
    # dest2 = Destination()
    # dest2.img = "destination_2.jpg"
    # dest2.name = "Delhi"
    # dest2.desc = "City always sleeps"
    # dest2.price = "From $ 650"
    # dest2.offer = False
    #
    # dest3 = Destination()
    # dest3.img = "destination_3.jpg"
    # dest3.name = "Chennai"
    # dest3.desc = "City never wakes"
    # dest3.price = "From $ 350"
    # dest3.offer = True
    #
    # dest4 = Destination()
    # dest4.img = "destination_7.jpg"
    # dest4.name = "Hyderabad"
    # dest4.desc = "City never drinks"
    # dest4.price = "From $ 850"
    # dest4.offer = False
    #
    # dest5 = Destination()
    # dest5.img = "destination_8.jpg"
    # dest5.name = "Banglore"
    # dest5.desc = "City always works"
    # dest5.price = "From $ 750"
    # dest5.offer = True
    #
    # dest6 = Destination()
    # dest6.img = "destination_9.jpg"
    # dest6.name = "Tamil Nadu"
    # dest6.desc = "City never eats"
    # dest6.price = "From $ 250"
    # dest6.offer = True
    #
    # dests = [dest1, dest2, dest3, dest4, dest5, dest6]
    dests = Destination.objects.all()
    return render(request, "index.html", {"dests": dests})


def home(request):
    return render(request, "travello/home.html")


def contact(request):
    return render(request, "travello/contact.html")
