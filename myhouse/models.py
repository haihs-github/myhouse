from django.db import models

# Create your models here.

class Phong(models.Model):
	sodienthangtruoc = models.BigIntegerField(default=0)
	sonuocthangtruoc = models.BigIntegerField(default=0)
	sodienthangnay = models.BigIntegerField(default=0)
	sonuocthangnay = models.BigIntegerField(default=0)
	tiennha = models.BigIntegerField(default=0)

class Congno(models.Model):
	thang = models.CharField(max_length=255)
	tiennha = models.BigIntegerField(default=0)
	tiennuoc = models.BigIntegerField(default=0)
	tiendien = models.BigIntegerField(default=0)
	trangthai = models.BooleanField(default=False)
	cuaphong = models.ForeignKey(Phong, on_delete=models.PROTECT, related_name='cuaphong',default=0)




