from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('phong/<int:id>', views.phong, name='index'),
	path('cal', views.cal, name='cal'),
	path('subform', views.subform, name='subform'),

]
