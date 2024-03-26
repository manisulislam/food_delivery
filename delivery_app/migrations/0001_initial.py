# Generated by Django 4.2.7 on 2024-03-26 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organizaion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone', models.CharField(max_length=20)),
                ('fixed_price', models.DecimalField(decimal_places=2, default=10, max_digits=10)),
                ('base_distance_in_km', models.IntegerField(default=10)),
                ('km_in_price', models.CharField(choices=[('perishable', '1.5'), ('non-perishable', '1')], max_length=20)),
                ('item_type', models.CharField(blank=True, choices=[('perishable', 'perishable'), ('non-perishable', 'non-perishable')], max_length=20, null=True)),
                ('item_description', models.TextField(blank=True, null=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery_app.organizaion')),
            ],
        ),
    ]
