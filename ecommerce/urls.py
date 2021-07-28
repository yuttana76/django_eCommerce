"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

# from products.views import (
#     ProductListView, 
#     product_list_view ,
#     ProductDetailView, 
#     productDetailSlugView,
#     ProductDetailSlugView,
#     product_detail_view,
#     ProductFeatureListView,
#     ProductFeatureDetailView
#     )

from .view import home_page, about_page, contact_page,login_page,register_page

urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('contact/', contact_page, name='contact'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('bootstrap/', TemplateView.as_view(template_name='bootstrap/example.html')),
    path('products/', include("products.urls")),
    path('search/', include("search.urls")),

    # path('featured/', ProductFeatureListView.as_view()),
    # path('featured/<int:pk>', ProductFeatureDetailView.as_view()),
    # path('products/', ProductListView.as_view()),
    # path('products-fbv/', product_list_view),
    # path('products/<int:pk>/', ProductDetailView.as_view()),
    # # path('products/<str:slug>/', productDetailSlugView),
    # path('products/<str:slug>/', ProductDetailSlugView.as_view()),
    # path('products-fbv/<int:pk>', product_detail_view),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)