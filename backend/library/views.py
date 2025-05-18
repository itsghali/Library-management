from rest_framework import generics, permissions, status
from .models import Book, Borrow, Reservation
from .serializers import BookSerializer, BorrowSerializer, ReservationSerializer, UserRegisterSerializer,BorrowCreateSerializer
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from django.contrib.auth import authenticate


# --- AUTHENTICATION VIEWS ---
class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.id,
                'username': user.username,
                'is_staff': user.is_staff
            })
        else:
            return Response(
                {'detail': 'Invalid credentials'}, 
                status=status.HTTP_401_UNAUTHORIZED
            )


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        # Create token for the new user
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
            'token': token.key,
            'user_id': user.id,
            'username': user.username
        }, status=status.HTTP_201_CREATED)


class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


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
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer


class BorrowCreateView(generics.CreateAPIView):
    queryset = Borrow.objects.all()  # Create a new borrow
    serializer_class = BorrowSerializer  # Use the BorrowSerializer to create a new borrow


class BorrowRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Borrow.objects.all()  # Get a borrow by pk
    serializer_class = BorrowSerializer  # Use the BorrowSerializer for detail, update, or delete

class BorrowCreateView(generics.CreateAPIView):
    queryset = Borrow.objects.all()
    serializer_class = BorrowCreateSerializer



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


# --- USER VIEWS ---
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]  # Only admin users can list users


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = []  # Ou [AllowAny] si tu veux le rendre public


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'login': reverse('login', request=request, format=format),
        'register': reverse('register', request=request, format=format),
        'profile': reverse('user-profile', request=request, format=format),
        'books': reverse('book-list', request=request, format=format),
        'borrows': reverse('borrow-list', request=request, format=format),
        'reservations': reverse('reservation-list', request=request, format=format),
        'users': reverse('user-list', request=request, format=format),
    })