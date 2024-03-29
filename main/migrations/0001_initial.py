# Generated by Django 4.2.4 on 2024-01-22 10:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(blank=True, max_length=55, null=True)),
                ('subject', models.CharField(blank=True, max_length=55, null=True)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('year_started', models.PositiveIntegerField()),
                ('year_ended', models.PositiveIntegerField(blank=True, null=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images_portfolio/')),
            ],
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('percentage', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('img', models.ImageField(upload_to='img_testimonial/')),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('category', models.CharField(max_length=255)),
                ('client', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('url', models.URLField()),
                ('img', models.ManyToManyField(to='main.images')),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('about_title', models.CharField(max_length=255)),
                ('birthday', models.DateField()),
                ('phone', models.CharField(blank=True, max_length=13, null=True, validators=[django.core.validators.RegexValidator(code='invalid_number', message='Invalid phone number', regex='^[\\+]9{2}8{1}[0-9]{9}$')], verbose_name='Telefon raqam')),
                ('address', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('degree', models.IntegerField(choices=[(1, 'Junior'), (2, 'Middle'), (3, 'Senior')])),
                ('freelance', models.CharField(max_length=255)),
                ('about_text', models.TextField()),
                ('img', models.ImageField(upload_to='img_about/')),
                ('email', models.EmailField(max_length=254)),
                ('telegram', models.CharField(max_length=255)),
                ('github', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('website', models.URLField()),
                ('education', models.TextField()),
                ('happy_clients', models.PositiveIntegerField()),
                ('projects', models.PositiveIntegerField()),
                ('hours_of_support', models.PositiveIntegerField()),
                ('awards', models.PositiveIntegerField()),
                ('location', models.CharField(max_length=255)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_call', models.CharField(max_length=20)),
                ('experiences', models.ManyToManyField(to='main.experience')),
                ('profession', models.ManyToManyField(to='main.profession')),
                ('services', models.ManyToManyField(to='main.service')),
                ('skills', models.ManyToManyField(to='main.skill')),
                ('testimonials', models.ManyToManyField(to='main.testimonial')),
                ('web_img', models.ManyToManyField(to='main.images')),
            ],
        ),
    ]
