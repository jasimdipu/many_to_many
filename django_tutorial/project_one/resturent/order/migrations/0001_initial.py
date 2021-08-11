# Generated by Django 3.1.5 on 2021-02-05 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('foods', '0003_food_foodcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=200)),
                ('order_number', models.CharField(max_length=200)),
                ('table_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('discount', models.FloatField(default=0.0)),
                ('food_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='foods.food')),
                ('orders', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='order.order')),
            ],
        ),
    ]