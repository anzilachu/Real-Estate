from django.shortcuts import render,redirect
from .models import Listings
from .forms import ListingForm

def listings_list(request):
    # models map by importing it
    listings = Listings.objects.all()
    context = {
        "listings" : listings
    }
    return render(request,"listings.html",context)


def listings_retrieve(request,pk):
    listing = Listings.objects.get(id=pk)
    context = {
        "listing":listing
    }
    return render(request,"listing.html",context)


def listings_create(request):
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {
        "form" : form
    }

    return render(request,"create.html",context)


def listings_update(request,pk):
    listupdate = Listings.objects.get(id=pk)
    form = ListingForm(instance=listupdate)
    if request.method == "POST":
        form = ListingForm(request.POST,instance=listupdate)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {
        "form" : form
    }

    return render(request,"update.html",context)


def listings_delete(request,pk):
    listings = Listings.objects.get(id=pk)
    listings.delete()
    return redirect('/')