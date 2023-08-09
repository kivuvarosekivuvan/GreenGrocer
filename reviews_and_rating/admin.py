from django.contrib import admin
from .models import Reviews_and_Ratings

class Reviews_and_RatingsAdmin(admin.ModelAdmin):
    list_display = ("title", "review_Content", "rating", "cumulative_ratings", "author", 'created_date')

admin.site.register(Reviews_and_Ratings, Reviews_and_RatingsAdmin)
