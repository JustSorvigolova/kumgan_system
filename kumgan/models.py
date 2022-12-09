from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

now = timezone.now()


class Box(models.Model):
    number_of_box = models.SmallIntegerField(default=0)
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.number_of_box)

    def get_absolute_url(self):
        return '/box_list'

    class Meta:
        verbose_name = 'Box'
        verbose_name_plural = 'Boxes'


class Schedule(models.Model):
    time_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=False)
    box = models.ForeignKey(Box, on_delete=models.CASCADE, related_name='box')
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.time_date)

    def get_box_box(self):
        return self.box.number_of_box

    def get_absolute_url(self):
        return '/schedule_list'

    class Meta:
        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedules'


class Category_Transport(models.Model):
    type_of_car = models.CharField(max_length=20)

    def __str__(self):
        return self.type_of_car

    def get_absolute_url(self):
        return '/category_list'

    class Meta:
        verbose_name = 'Category_Transport'
        verbose_name_plural = 'Category_Transports'


class Services(models.Model):
    title_service = models.CharField(max_length=20)
    price_service = models.IntegerField(verbose_name='Цена')
    amount = models.IntegerField(default=1, verbose_name="Количество")
    category_transport = models.ForeignKey(Category_Transport,
                                           on_delete=models.CASCADE, related_name="category_transport")

    def __str__(self):
        return str(self.title_service)

    def get_name_of_service(self):
        return self.title_service

    def get_price(self):
        return self.price_service

    def get_total_item_price(self):
        return self.amount * self.get_price()

    def get_final_price(self):
        return self.get_total_item_price()

    def get_absolute_url(self):
        return '/price_list'

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class Booking(models.Model):
    """Бронирование"""
    category_transport = models.ForeignKey(Category_Transport,
                                           on_delete=models.CASCADE, related_name="category_transport_booking")
    time_and_date = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name="time_and_date")
    title_service = models.ManyToManyField(Services, related_name="title_service_booking")
    number_car = models.CharField(max_length=6)
    status = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for product in self.title_service.all():
            total += product.get_final_price()
        return total

    def get_box(self):
        box = self.time_and_date.get_box_box()
        return box

    def get_service(self):
        service = ''
        for i in self.title_service.all():
            service = i.get_name_of_service()
        return service

    def get_price_each(self):
        price = 0
        for i in self.title_service.all():
            price = i.get_price()
        return price

    def get_absolute_url(self):
        return '/home'

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'
