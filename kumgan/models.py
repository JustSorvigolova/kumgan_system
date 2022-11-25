from django.db import models
from django.contrib.auth.models import User


class Box(models.Model):
    number_of_box = models.SmallIntegerField(default=0)

    def __str__(self):
        return str(self.number_of_box)

    class Meta:
        verbose_name = 'Box'
        verbose_name_plural = 'Boxs'


class Schedule(models.Model):
    time = models.TimeField(auto_now=False, auto_now_add=False)
    date = models.DateField(auto_now=False, auto_now_add=False)
    box = models.ForeignKey(Box, on_delete=models.CASCADE, related_name='box')
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.date) and str(self.date)

    class Meta:
        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedules'


class Category_Transport(models.Model):
    type_of_car = models.CharField(max_length=20)

    def __str__(self):
        return "Категории Транспорта"

    class Meta:
        verbose_name = 'Category_Transport'
        verbose_name_plural = 'Category_Transports'


class Services(models.Model):
    title_service = models.CharField(max_length=20)
    price_service = models.IntegerField(verbose_name='Цена')
    category_transport = models.ForeignKey(Category_Transport,
                                           on_delete=models.CASCADE, related_name="category_transport")

    def __str__(self):
        return self.title_service

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class Booking(models.Model):
    """Бронирование"""
    category_transport = models.ForeignKey(Category_Transport,
                                           on_delete=models.CASCADE, related_name="category_transport_booking")
    time_and_date = models.OneToOneField(Schedule, on_delete=models.CASCADE, related_name="time_and_date")
    title_service = models.ManyToManyField(Services, related_name="title_service_booking")
    number_car = models.CharField(max_length=6)
    total = models.IntegerField()
    status = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")

    def calculate_total_price(self):
        total = self.total + Services.price_service
        return total

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'
