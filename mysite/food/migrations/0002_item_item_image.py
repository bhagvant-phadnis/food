# Generated by Django 4.2 on 2024-11-23 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://plakarestaurant.ca/wp-content/themes/twentytwentythree-child/img/food-placeholder.png', max_length=500),
        ),
    ]