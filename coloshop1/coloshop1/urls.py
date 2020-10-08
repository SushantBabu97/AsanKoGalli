"""coloshop1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from cms.views import SignUpView

from shop.views import HomepageView, ProductView, CategoryApiView, some_view, CategoryView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomepageView.as_view()),
    path('products/<int:product_id>', ProductView.as_view(), name='product_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup', SignUpView.as_view(), name='signup'),
    path('api/categories', CategoryApiView.as_view()),
    path('category-report', some_view),
    path('category/<int:category_id>', CategoryView.as_view(), name='category_detail')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
