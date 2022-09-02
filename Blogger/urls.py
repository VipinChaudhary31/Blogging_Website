from django.urls import path, include
from .views import HomeView

urlpatterns = [
    path('', HomeView, name='Home'),
    # path('Verification/', include('django.contrib.auth.urls')),
    # path("Verification/",include('Verification.urls'))

]
