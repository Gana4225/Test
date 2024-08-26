from django.urls import path,include


from .views import std,apiv,create,list,retrieve,update,destroy,lc,ru,rd,rud
from .views import lmm

urlpatterns=[
    path('hi/',std),
    path('tata/<int:tt>',apiv.as_view()),
    path('tata/',apiv.as_view()),
    path('tata/l/',list.as_view()),
    path('tata/c/',create.as_view()),
    path('tata/r/<int:pk>/',retrieve.as_view()),
    path('tata/u/<int:pk>/',update.as_view()),
    path('tata/d/<int:pk>/',destroy.as_view()),
    path('tata/lc/',lc.as_view()),
    path('tata/ru/<int:pk>/',ru.as_view()),
    path('tata/rd/<int:pk>/',rd.as_view()),
    path('tata/rud/<int:pk>/',rud.as_view()),
    path('tata/lmm/',lmm.as_view()),
    
]