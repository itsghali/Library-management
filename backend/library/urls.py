from django.urls import path
from .views import (
    BookListView, BookCreateView, BookRetrieveUpdateDestroyView,
    BorrowListView, BorrowCreateView, BorrowRetrieveUpdateDestroyView,
    ReservationListView, ReservationCreateView, ReservationRetrieveUpdateDestroyView,
    UserListView, UserCreateView, UserRetrieveUpdateDestroyView,
    LoginView, RegisterView, UserProfileView
)

urlpatterns = [

    # Authentication
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),

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


# Users (Admin only)
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
]