# Generated by Django 2.1.5 on 2020-10-26 21:15

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('signup', '0003_auto_20201021_1830'),
    ]

    operations = [
        migrations.CreateModel(
            name='flat',
            fields=[
                ('id', models.AutoField(help_text='Unique ID for this particular flat', primary_key=True, serialize=False)),
                ('warehouse', models.BooleanField(default=False)),
                ('city', models.CharField(max_length=254)),
                ('country', models.CharField(max_length=254)),
                ('district', models.CharField(max_length=254)),
                ('location', models.CharField(max_length=254)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='flatDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smart_tv', models.BooleanField(default=False)),
                ('computer', models.BooleanField(default=False)),
                ('modern_radio', models.BooleanField(default=False)),
                ('conditioner', models.BooleanField(default=False)),
                ('humidifier', models.BooleanField(default=False)),
                ('smart_frige', models.BooleanField(default=False)),
                ('lights_on_time', models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MaxValueValidator(23), django.core.validators.MinValueValidator(0)])),
                ('flat', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='signup.flat')),
            ],
        ),
    ]
