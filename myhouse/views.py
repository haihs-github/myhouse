from django.shortcuts import render, redirect
from .models import Phong, Congno

# Create your views here.

def index(request):
	return render(request, 'index.html')

def phong(request, id):
	# phong = Phong.objects.get(id=id)
	# sodien = phong.sodienthangnay - phong.sodienthangtruoc
	# sonuoc = phong.sonuocthangnay - phong.sonuocthangtruoc
	# tiendien = 0
	# tiennuoc = 0
	# if sodien > 150:
	# 	tiendien = (sodien-150)*3500 + 150*3500
	# else:
	# 	tiendien = sodien*3500
	# tiennuoc = sonuoc*18000
	# tong = tiendien + tiennuoc
	# trangthai =  phong.congno.trangthai
	# tiendien = phong.congno.tiendien
	# tiennuoc = phong.congno.tiennuoc
	# context = {
	# 	'phong': phong,
	# 	'sodien': sodien,
	# 	'sonuoc': sonuoc,
	# 	'tiendien': tiendien,
	# 	'tiennuoc': tiennuoc,
	# 	'tong': tong,
	# 	'trangthai': trangthai,
	# }
	return render(request, 'phong.html', context)

def cal(request):
	# phongs = Phong.objects.all()
	# context = {
	# 	'phongs': phongs,
	# }
	return render(request, 'cal.html', context)

def subform(request):
	# phongs = Phong.objects.all()
	# for x in phongs:
	# 	postdien = f'sodienphong{x.id}'
	# 	postnuoc = f'sonuocphong{x.id}'
	# 	x.sodienthangtruoc = x.sodienthangnay
	# 	x.sodienthangnay = request.POST[postdien]
	# 	x.sonuocthangtruoc = x.sonuocthangnay
	# 	x.sonuocthangnay = request.POST[postnuoc]
	# 	x.save()
	return redirect('/')
	