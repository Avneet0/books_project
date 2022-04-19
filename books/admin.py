from django.contrib import admin

# Register your models here.
from .models import Books

# class ReviewInline(admin.TabularInline):
#     model = Review
# class BookAdmin(admin.ModelAdmin):
#     inlines = [
#     ReviewInline,
#     ]
#     list_display = ("title", "author", "price",)


admin.site.register(Books)