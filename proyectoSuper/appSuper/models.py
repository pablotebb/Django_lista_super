from django.core.exceptions import ValidationError
from django.db import models

def validate_three_digits(value):
  if value < 0 or value > 999:
    raise ValidationError('Asegurate de tener este valor entr 0 y 999.')

class Item(models.Model):
  s_name = models.CharField(max_length=100)
  d_price = models.DecimalField(max_digits=10, decimal_places=2)
  i_quantity = models.IntegerField(validators=[validate_three_digits], default=0)
  b_checked = models.BooleanField(default=False)

  def __str__(self):
    return self.s_name
