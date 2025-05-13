from rest_framework import generics
from .models import Book, Borrow, Reservation
from .serializers import BookSerializer, BorrowSerializer, ReservationSerializer


# --- BOOK VIEWS ---
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()  # Get all books from the database
    serializer_class = BookSerializer  # Use the BookSerializer to list the books


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()  # Create a new book
    serializer_class = BookSerializer  # Use the BookSerializer to create a new book


class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()  # Get a book by pk
    serializer_class = BookSerializer  # Use the BookSerializer for detail, update, or delete


# --- BORROW VIEWS ---
class BorrowListView(generics.ListAPIView):
    queryset = Borrow.objects.all()  # Get all borrows from the database
    serializer_class = BorrowSerializer  # Use the BorrowSerializer to list the borrows


class BorrowCreateView(generics.CreateAPIView):
    queryset = Borrow.objects.all()  # Create a new borrow
    serializer_class = BorrowSerializer  # Use the BorrowSerializer to create a new borrow


class BorrowRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Borrow.objects.all()  # Get a borrow by pk
    serializer_class = BorrowSerializer  # Use the BorrowSerializer for detail, update, or delete


# --- RESERVATION VIEWS ---
class ReservationListView(generics.ListAPIView):
    queryset = Reservation.objects.all()  # Get all reservations from the database
    serializer_class = ReservationSerializer  # Use the ReservationSerializer to list the reservations


class ReservationCreateView(generics.CreateAPIView):
    queryset = Reservation.objects.all()  # Create a new reservation
    serializer_class = ReservationSerializer  # Use the ReservationSerializer to create a new reservation


class ReservationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()  # Get a reservation by pk
    serializer_class = ReservationSerializer  # Use the ReservationSerializer for detail, update, or delete
