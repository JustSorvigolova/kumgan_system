# Generated by Django 4.1.3 on 2022-12-10 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_box', models.SmallIntegerField(default=0)),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Box',
                'verbose_name_plural': 'Boxes',
            },
        ),
        migrations.CreateModel(
            name='Category_Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_car', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Category_Transport',
                'verbose_name_plural': 'Category_Transports',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_service', models.CharField(max_length=20)),
                ('price_service', models.IntegerField(verbose_name='Цена')),
                ('amount', models.IntegerField(default=1, verbose_name='Количество')),
                ('category_transport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_transport', to='kumgan.category_transport')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_date', models.DateTimeField()),
                ('status', models.BooleanField(default=False)),
                ('box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='box', to='kumgan.box')),
            ],
            options={
                'verbose_name': 'Schedule',
                'verbose_name_plural': 'Schedules',
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_car', models.CharField(max_length=6)),
                ('status', models.BooleanField(default=False)),
                ('category_transport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_transport_booking', to='kumgan.category_transport')),
                ('time_and_date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time_and_date', to='kumgan.schedule')),
                ('title_service', models.ManyToManyField(related_name='title_service_booking', to='kumgan.services')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Booking',
                'verbose_name_plural': 'Bookings',
            },
        ),
    ]
