from django.contrib import admin
from .models import Congno, Phong
# Register your models here.



# Register your models here.

class CongnoAdmin(admin.ModelAdmin):
	list_display = ("id", "thang", "tiennha", "tiennuoc", "tiendien", "trangthai, cuaphong")

class PhongAdmin(admin.ModelAdmin):
	list_display = ("id", "sodienthangtruoc", "sodienthangnay", "sonuocthangtruoc", "sonuocthangnay","tiennha")

admin.site.register(Phong, PhongAdmin)
admin.site.register(Congno, CongnoAdmin)