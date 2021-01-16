from django.shortcuts import render, get_object_or_404
from .models import Category, Listing, Review
from .forms import ReviewForm
from django.core.paginator import Paginator, EmptyPage, \
                                  PageNotAnInteger

# Create your views here.
def home(request):
    return render(request, 'listing/home.html')

def business_list(request):
    object_list = Listing.objects.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        listings = paginator.page(page)
    except PageNotAnInteger:
        listings = paginator.page(1)
    except EmptyPage:
        listings = paginator.page(paginator.num_pages)
    return render(request, 'listing/list.html', {'listings': listings,
                                                 'page': page})

def list_detail(request, year, month, day, listing):
    listing = get_object_or_404(Listing, slug=listing, status='published',
                               publish__year=year,
                               publish__month=month,
                               publish__day=day)
    reviews = listing.reviews.filter(active=True)
    new_review = None
    if request.method == 'POST':
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.listing=listing
            new_review.save()
    else:
        review_form = ReviewForm()
    return render(request, 'listing/detail.html', {'listing': listing, 'reviews': reviews,
                                                   'new_review': new_review,
                                                   'review_form': review_form})

def search(request):
    listings = Listing.objects.filter(name__contains=request.GET['name'])
    return render(request, 'listing/list.html', {'listings': listings})

