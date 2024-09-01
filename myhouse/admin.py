from django.contrib import admin
from .models import Congno, Phong
# Register your models here.



# Register your models here.

class CongnoAdmin(admin.ModelAdmin):
	list_display = ("tiennha", "tiennuoc", "tiendien", "trangthai")

class PhongAdmin(admin.ModelAdmin):
	list_display = ("sodienthangtruoc", "sodienthangnay", "sonuocthangtruoc", "sonuocthangnay","tiennha")

admin.site.register(Phong, PhongAdmin)
admin.site.register(Congno, CongnoAdmin)