
from django.db import models
from django.urls import reverse
from django.conf import settings

class Coin(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    country = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='coin_images/', blank=True, null=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='coins',
        null=True,
        blank=True,
        help_text='User that created/owns this coin'
    )

    def __str__(self):
        return f"{self.name} ({self.year})"

    def get_absolute_url(self):
        return reverse('coin-detail', kwargs={'coin_id': self.id})

class GlobalRank(models.Model):
    date = models.DateField('Ranking Date')
    rank = models.IntegerField()
    source = models.CharField(max_length=100, blank=True)
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)

    def __str__(self):
        return f"Rank {self.rank} for {self.coin.name} on {self.date}"
    class Meta:
        ordering = ['-date']  
