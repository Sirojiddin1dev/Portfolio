from django.db import models
from django.core.validators import RegexValidator


class Images(models.Model):
    img = models.ImageField(upload_to='images_portfolio/')


class Experience(models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    year_started = models.PositiveIntegerField()
    year_ended = models.PositiveIntegerField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=255)
    percentage = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    author = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    content = models.TextField()
    img = models.ImageField(upload_to='img_testimonial/')

    def __str__(self):
        return self.author


class Profession(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    # Personal Information
    full_name = models.CharField(max_length=255)
    profession = models.ManyToManyField(Profession)

    # About Section
    about_title = models.CharField(max_length=255)
    birthday = models.DateField()
    phone = models.CharField(max_length=13, verbose_name='Telefon raqam', null=True, blank=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid_number'
        ), ])
    address = models.CharField(max_length=255)
    age = models.IntegerField()
    Degree = (
        ('Junior', 'junior'),
        ('Middle', 'middle'),
        ('Senior', 'senior')
    )
    degree = models.CharField(max_length=50, choices=Degree)
    freelance = models.CharField(max_length=255)
    about_text = models.TextField()
    img = models.ImageField(upload_to='img_about/')

    # Contact Information
    email = models.EmailField()
    telegram = models.CharField(max_length=255)
    github = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    website = models.URLField()

    # Education
    education = models.TextField()

    # Professional Experience
    experiences = models.ManyToManyField(Experience)

    # Skills
    skills = models.ManyToManyField(Skill)

    # Facts Section
    happy_clients = models.PositiveIntegerField()
    projects = models.PositiveIntegerField()
    hours_of_support = models.PositiveIntegerField()
    awards = models.PositiveIntegerField()

    # Services
    services = models.ManyToManyField(Service)

    # Testimonials
    testimonials = models.ManyToManyField(Testimonial)

    # Contact Section
    location = models.CharField(max_length=255)
    contact_email = models.EmailField()
    contact_call = models.CharField(max_length=20)

    # img section
    web_img = models.ManyToManyField(Images)

    def __str__(self):
        return self.full_name


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=55, null=True, blank=True)
    subject = models.CharField(max_length=55, null=True, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name


class PortfolioDetail(models.Model):
    img = models.ManyToManyField(Images)
    title = models.CharField(max_length=255)
    text = models.TextField()
    category = models.CharField(max_length=255)
    client = models.CharField(max_length=255)
    date = models.DateField()
    url = models.URLField()

    def __str__(self):
        return self.title
