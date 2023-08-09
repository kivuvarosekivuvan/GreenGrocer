from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import Reviews_and_Ratings
from .forms import ReviewForm

def review_list(request):
    reviews = Reviews_and_Ratings.objects.all()
    return render(request, 'reviews/review_list.html', {'reviews': reviews})

def review_detail(request, review_id):
    review = get_object_or_404(Reviews_and_Ratings, id=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})

def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review_list')
    else:
        form = ReviewForm()
    return render(request, 'reviews/create_review.html', {'form': form})
