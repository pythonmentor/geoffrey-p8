# Generated by Django 3.0.5 on 2020-04-09 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('barcode', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=80)),
                ('brand', models.CharField(max_length=80)),
                ('url', models.URLField()),
                ('nutrition_grade', models.CharField(max_length=1)),
                ('nutrition_score', models.SmallIntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Category')),
            ],
        ),
    ]