from django.urls import path
from .views import BookListCreateView, BookDetailAPIView

urlpatterns = [
    path('', BookListCreateView.as_view(), name='book-list'),
    path('<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
]
