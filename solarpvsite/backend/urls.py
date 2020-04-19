from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('products', views.ProductView)
router.register('certificates', views.CertificateView)
router.register('services', views.ServiceView)

urlpatterns = [
    path('', include(router.urls))
]