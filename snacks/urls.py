from django.urls import path
from .views import SnackListView, SnackDetailView, SnackCreateView, SnackDeleteView, SnackUpdateView, HomePageView

urlpatterns = [
    path('', SnackListView.as_view(), name='list_snack'),
    path('<int:pk>/', SnackDetailView.as_view(), name='detail_snack'),
    path('create/', SnackCreateView.as_view(), name='create_snack'),
    path('update/<int:pk>/', SnackUpdateView.as_view(), name='update_snack'),
    path('delete/<int:pk>/', SnackDeleteView.as_view(), name='delete_snack'),
    path('', HomePageView.as_view(), name='home'),
    ]