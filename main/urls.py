from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name="index_url"),
    path('create-contact', create_contact_view, name="create_contact_url"),
    path('portfolio-detail', portfolio_detail_view, name="portfolio_detail_url"),
]
