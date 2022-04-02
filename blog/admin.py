from django.contrib import admin
from .models import Book, Meetup


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'author', 'year_published', 'members_rating', 'has_been_read')
    prepopulated_fields = {'slug': ('title',)}
    # list_filter = ('has_been_read')


@admin.register(Meetup)
class MeetupAdmin(admin.ModelAdmin):
    
    list_display = ('long_title', 'meetup_date', 'book1')
    prepopulated_fields = {'slug': ('title',)}
