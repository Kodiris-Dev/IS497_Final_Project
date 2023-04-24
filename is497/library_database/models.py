from django.db import models

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % self.name


class Language(models.Model):
    language_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % self.name


class Membership(models.Model):
    membership_id = models.AutoField(primary_key=True)
    # name = models.CharField(max_length=50, default="")
    membership_class = models.CharField(max_length=50, default="")

    def __str__(self):
        return '%s' % self.membership_class


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=50, default="")
    zip = models.IntegerField()
    contact_number = models.CharField(max_length=20)
    preferred_genre = models.ForeignKey(Genre, related_name='profiles', on_delete=models.PROTECT)
    preferred_language = models.ForeignKey(Language, related_name='profiles', on_delete=models.PROTECT)
    membership_type = models.ForeignKey(Membership, related_name='profiles', on_delete=models.PROTECT)
    assistance = models.BooleanField()

    def __str__(self):
        return '%s - %s' % (self.user.last_name, self.user.first_name)


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    isbn = models.IntegerField()
    edition = models.IntegerField()
    genre = models.ForeignKey(Genre, related_name='books', on_delete=models.PROTECT)
    publication_date = models.DateTimeField(default=timezone.now)
    sample_text = models.CharField(max_length=300)
    # review_id = models.ForeignKey(review_id)
    language = models.ForeignKey(Language, related_name='books', on_delete=models.PROTECT)

    def __str__(self):
        return '%s - %s' % (self.title, self.author)


class Magazine(models.Model):
    magazine_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    volume = models.IntegerField()
    edition = models.IntegerField()
    genre = models.ForeignKey(Genre, related_name='magazines', on_delete=models.PROTECT)
    publication_date = models.DateTimeField(default=timezone.now)
    sample_page = models.CharField(max_length=300)
    # review_id = models.ForeignKey(review_id)
    language = models.ForeignKey(Language, related_name='magazines', on_delete=models.PROTECT)

    def __str__(self):
        return '%s - %s' % (self.title, self.volume)


class DVD(models.Model):
    dvd_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    studio = models.CharField(max_length=50)
    volume = models.IntegerField()
    genre = models.ForeignKey(Genre, related_name='dvds', on_delete=models.PROTECT)
    production_date = models.DateTimeField(default=timezone.now)
    digital = models.BooleanField
    # review_id = models.ForeignKey(review_id)
    language = models.ForeignKey(Language, related_name='dvds', on_delete=models.PROTECT)

    def __str__(self):
        return '%s' % self.title


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.AutoField(primary_key=True)
    work_schedule = models.CharField(max_length=50, default="")
    work_hours = models.CharField(max_length=50, default="")
    title = models.CharField(max_length=50, default="")
    status = models.CharField(max_length=20, default="")
    start_date = models.DateTimeField()
    profile_access = models.BooleanField()
    user_access = models.BooleanField()
    employee_access = models.BooleanField()
    book_access = models.BooleanField()
    magazine_access = models.BooleanField()
    dvd_access = models.BooleanField()

    def __str__(self):
        return '%s' % (self.user.username)





