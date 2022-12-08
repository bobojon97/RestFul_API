from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Car(models.Model):
    vin = models.CharField(verbose_name='Вин', db_index=True, unique=True, max_length=60)
    color = models.CharField(verbose_name='Цвет', max_length=60)
    brand = models.CharField(verbose_name='Brand', max_length=64)
    CAR_TYPES = (
        (1, 'Седан'),
        (2, 'Хечбек'),
        (3, 'Универсал'),
        (4, 'Купе'),
    )
    car_type = models.IntegerField(verbose_name='Car_Type', choices=CAR_TYPES)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)