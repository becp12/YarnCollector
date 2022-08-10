from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator
# from datetime import date

UNITS = (
    ('B', 'Ball'),
    ('S', 'Skein'),
    ('G', 'Grams'),
    ('O', 'Ounces')
)

# Create your models here.

class Yarn(models.Model):
    brand = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    color = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.brand} {self.name} ({self.id})'
        
    def get_absolute_url(self):
        return reverse('detail', kwargs={'cat.id':self.id})

    # def yarn_remaining(self):
    #     quantBeforeToday = self.quantity_set.filter(date__lte = datetime.now())
    #     return quantBeforeToday.count == 0 or quantBeforeToday.first().amount > 0



class Quantity(models.Model):
    date = models.DateField('Quantity as of Date')
    amount = models.FloatField('Amount of Yarn left', validators=[MinValueValidator(0.0)])
    unit = models.CharField(
        'Unit of Measurement',
        max_length=1,
        choices=UNITS,
        default=UNITS[0][0]
    )
    
    yarn = models.ForeignKey(
        Yarn,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.amount} {self.get_unit_display()} on {self.date}'

    class Meta:
        ordering = ['-date']

    