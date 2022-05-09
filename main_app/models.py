from django.db import models
from django.urls import reverse

# Create your models here.
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Finch(models.Model):
    name = models.CharField(max_length=20)
    height = models.CharField(max_length=20)
    vertical = models.IntegerField()

    def _str_(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})

class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
        )
    finch = models.ForeignKey(
        Finch,
        on_delete=models.CASCADE
    )

    def _str_(self):
        return f"{self.get_meal_display()} on {self.date}"

    class Meta:
        ordering = ['-date']
