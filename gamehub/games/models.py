from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    trailer_url = models.URLField(max_length=200, blank=True, null=True)
    cover_image = models.ImageField(upload_to='games/', blank=True, null=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='reviews')
    user_name = models.CharField(max_length=100)
    rating = models.PositiveIntegerField()  # امتیاز بازی (مثلاً از 1 تا 5)
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.game.title} by {self.user_name}"
