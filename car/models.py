from django.db import models

from user.models import User


class CarBrand(models.Model):
    brand = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.brand)


class CarModel(models.Model):
    model = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.model)


class Car(models.Model):
    brand = models.OneToOneField(to=CarBrand, on_delete=models.CASCADE)
    name = models.OneToOneField(to=CarModel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.brand} {self.name}"


class CarConfiguration(models.Model):
    car = models.ForeignKey(to=Car, on_delete=models.CASCADE)
    сolor = models.CharField(max_length=20)
    wheel = models.CharField(max_length=20)
    engine = models.CharField(max_length=20)
    will_arrive = models.DateField(verbose_name="Дата прибытия автомобиля", null=True)


class CarConfigurationOrder(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    configuration = models.ForeignKey(to=CarConfiguration, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return f"{self.user.get_full_name()} with price: {self.price}"


class Purchase(models.Model):
    buyer_first_name = models.CharField(max_length=150)
    buyer_second_name = models.CharField(max_length=150)
    configuration = models.ForeignKey(to=CarConfiguration, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self) -> str:
        return f"{self.buyer_first_name} {self.buyer_second_name}"
