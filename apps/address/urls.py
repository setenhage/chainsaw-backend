from django.urls import path
from apps.address import views

urlpatterns = [
    path('address_view/<int:pk>/', views.address_view),
    path('address_create/', views.address_create),
    # path('address_edit/<int:pk>/', views.address_edit),
    # path('address_delete/<int:pk>/', views.address_edit)
]