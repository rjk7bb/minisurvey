from django.urls import path
from . import views

app_name = 'survey'
urlpatterns = [

    path('1/', views.quest1),

    path('2/', views.quest2, name='q2'),

    path('3/', views.quest3, name='q3'),

    path('4/', views.quest4, name='q4'),

    path('5/', views.quest5, name='q5'),

    path('6/', views.quest6, name='q6'),

    path('7/', views.quest7, name='q7'),

    path('8/', views.quest8, name='q8'),

    path('10/', views.quest10, name='q10'),

    path('11/', views.quest11, name='q11'),

    path('12/', views.quest12, name='q12'),

    path('13/', views.quest13, name='q13'),

    path('14/', views.quest14, name='q14'),

    path('15/', views.quest15, name='q15')


]
