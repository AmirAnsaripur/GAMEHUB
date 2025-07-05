from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=150)
    platform = models.CharField(max_length=150)
    description = models.TextField()
    release_date = models.DateField(null=True)
    trailer_url = models.URLField(max_length=200, blank=True, null=True)
    cover_image = models.ImageField(upload_to='games/', blank=True, null=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='reviews')
    user_name = models.CharField(max_length=50)
    rating = models.PositiveIntegerField()
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
