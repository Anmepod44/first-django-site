from django.contrib import admin
from .models import Author,BookInstance,Book

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookInstance)

 