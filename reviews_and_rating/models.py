from django.db import models

class Reviews_and_Ratings(models.Model):
    title = models.CharField(max_length=32)
    review_Content = models.CharField(max_length=32)
    rating = models.IntegerField()
    cumulative_ratings = models.IntegerField()
    author = models.CharField(max_length=32)
    created_date = models.DateTimeField()

    class Meta:
        verbose_name_plural = "reviews_and_ratings"
