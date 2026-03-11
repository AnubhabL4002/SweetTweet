from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=280)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return f'{self.user.username} - {self.text[:10]}'

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, related_name='likes', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'tweet')  # prevent multiple likes

    def __str__(self):
        return f'{self.user.username} likes {self.tweet.id}'