from django.urls import path
from .views import BookListCreateView, BorrowListCreateView, ReservationListCreateView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list'),
    path('borrow/', BorrowListCreateView.as_view(), name='borrow-list'),
    path('reservation/', ReservationListCreateView.as_view(), name='reservation-list'),

    path('', BookListCreateView.as_view(), name='api-root'),
]