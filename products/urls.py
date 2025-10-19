from django.urls import path
from . import views
app_name = 'products'
urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:slug>/', views.category_view, name='category'),
    path('product/<int:pk>/', views.product_detail, name='detail'),
]
