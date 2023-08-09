from django import forms
from .models import Reviews_and_Ratings

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews_and_Ratings
        fields = ['title', 'review_Content', 'rating', 'cumulative_ratings', 'author', 'created_date']
