from django.urls import path
from .views import *

app_name="new_user"


urlpatterns=[

    path('home/',HomepageView.as_view(),name='home-page')
]