from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ecoblog.views import HomeView, ProtectedAreaDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'), 
    path('page/<int:pk>/', ProtectedAreaDetailView.as_view(), name='protected-area'), 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

