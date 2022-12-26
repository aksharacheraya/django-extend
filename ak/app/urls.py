from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('classes/',views.classes,name='classes'),
    path('contact/',views.contact,name='contact'),
    path('shortcodes/',views.shortcodes,name='shortcodes'),
    path('shows/',views.shows,name='shows'),
    path('test/',views.test,name='test'),

]
