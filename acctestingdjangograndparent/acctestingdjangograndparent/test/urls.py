from django.urls import path
from . import views

urlpatterns=[
    path('hello/',views.hello,name="hello"),
    path('langchoice/',views.langChoice,name='langchoice'),
    path('langchoice/docview/<int:pk>/',views.docview,name='docview')
]