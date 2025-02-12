# Generated by Django 4.0.1 on 2024-04-08 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('address', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('mail', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('publish_year', models.IntegerField(null=True)),
                ('num_of_page', models.IntegerField(null=True)),
                ('price', models.IntegerField(null=True)),
                ('stock', models.IntegerField(null=True)),
                ('sold', models.IntegerField(null=True)),
                ('cover', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.author')),
                ('categories', models.ManyToManyField(to='product.Category')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.publisher')),
            ],
        ),
    ]
