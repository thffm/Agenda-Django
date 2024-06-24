from django.contrib import admin
from contact import models




# Register your models here.
@admin.register(models.Contact)
class ContacAdmin(admin.ModelAdmin):
    list_display = 'id','frist_name','last','phone',
    ordering= 'id',
    search_fields = 'id','frist_name','last',
    list_per_page = 1
    list_max_show_all = 2
    list_editable = 'frist_name',
    list_display_links = 'last',
    ...
