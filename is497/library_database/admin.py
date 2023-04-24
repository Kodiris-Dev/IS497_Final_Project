from django.contrib import admin

from is497.library_database.models import Employee, Membership, Book, Magazine, DVD, Genre, Language, Profile

# Register your models here.
admin.site.register(Employee)
admin.site.register(Membership)
admin.site.register(Book)
admin.site.register(Magazine)
admin.site.register(DVD)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Profile)



