from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Auction
from products.models import Product
from bids.models import Bid



def all_auctions(request):
    
    # Create views for all auctions.
    # Let auctions available to only registered user/bidder
    # Else returns the unathorized user back to home 
    
    if request.user.is_authenticated:
        auctions = Auction.objects.filter()
        return render(request, "auction.html", {"auctions": auctions})
    else:
        messages.error(request, "You must be a registered user to view auctions!")
        return redirect(reverse('home'))
        
    return render(request, "home.html")
    

    

def one_auction(request):
    
    # Allow user to bid on a specifc product base on the start time and end time of an auction
    # If an auction time has ended a message is displayed to the user
    # If an auction time has not ended user can update thier bid
    
    if request.method == "POST":
       
            p_id = request.POST['product_id']
            auction = Auction.objects.get(product_id=p_id)
            if timezone.now() >= auction.start_time and timezone.now() < auction.end_time:
               
                product = Product.objects.get(id=p_id)
                product.auction_price += int(request.POST['Raise'])
                product.save()
                bids = Bid.objects.filter(product_id=p_id)
                if bids:
                    bid = bids[0]
                    bid.user_id = request.user
                    bid.bid_time = timezone.now()
                    bid.bid_views += 1
                    bid.save()
                
                else:
                    new_bid = Bid()
                    new_bid.product_id = product
                    new_bid.auction_id = auction
                    new_bid.user_id = request.user
                    new_bid.bid_time = timezone.now()
                    new_bid.bid_views += 1
                    new_bid.save()
                messages.error(request, "You have just raised your bid!")
            else:
                messages.error(request, "Auction has closed!")
            
    return redirect(reverse('auctions'))
        
        
    

        
   