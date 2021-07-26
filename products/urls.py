
from django.urls import path

from .views import (
    ProductListView, 
    # product_list_view ,
    # ProductDetailView, 
    # productDetailSlugView,
    ProductDetailSlugView,
    # product_detail_view,
    # ProductFeatureListView,
    # ProductFeatureDetailView
    )

app_name = 'products'
urlpatterns = [
    # path('featured/', ProductFeatureListView.as_view()),
    # path('featured/<int:pk>', ProductFeatureDetailView.as_view()),
    path('', ProductListView.as_view(), name='list'),
    # path('products-fbv/', product_list_view),
    # path('products/<int:pk>/', ProductDetailView.as_view()),
    
    # path('products/<str:slug>/', productDetailSlugView),
    path('<str:slug>/', ProductDetailSlugView.as_view(), name='detail'),
    
    # path('products-fbv/<int:pk>', product_detail_view),
]
