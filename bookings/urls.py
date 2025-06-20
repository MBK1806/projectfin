from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet, BookingViewSet, CustomAuthToken, RegisterView

router = DefaultRouter()
router.register(r'menu', MenuItemViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', CustomAuthToken.as_view()),
    path('registration/', RegisterView.as_view()),
]
