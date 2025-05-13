from django.urls import path
from .views import (
    BookListView, BookCreateView, BookRetrieveUpdateDestroyView,
    BorrowListView, BorrowCreateView, BorrowRetrieveUpdateDestroyView,
    ReservationListView, ReservationCreateView, ReservationRetrieveUpdateDestroyView
)

urlpatterns = [
    # Books
    path('books/', BookListView.as_view(), name='book-list'),  # List all books
    path('books/create/', BookCreateView.as_view(), name='book-create'),  # Create a new book
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),  # Retrieve, Update, or Delete a single book

    # Borrows
    path('borrows/', BorrowListView.as_view(), name='borrow-list'),  # List all borrows
    path('borrows/create/', BorrowCreateView.as_view(), name='borrow-create'),  # Create a new borrow
    path('borrows/<int:pk>/', BorrowRetrieveUpdateDestroyView.as_view(), name='borrow-detail'),  # Retrieve, Update, or Delete a single borrow

    # Reservations
    path('reservations/', ReservationListView.as_view(), name='reservation-list'),  # List all reservations
    path('reservations/create/', ReservationCreateView.as_view(), name='reservation-create'),  # Create a new reservation
    path('reservations/<int:pk>/', ReservationRetrieveUpdateDestroyView.as_view(), name='reservation-detail'),  # Retrieve, Update, or Delete a single reservation
]
