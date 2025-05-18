from rest_framework import serializers
from .models import Book, Borrow, Reservation
from django.contrib.auth.models import User

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def get_book(self, obj):
        return {
            "id": obj.book.id,
            "title": obj.book.title,
            "author": obj.book.author
        }


class ReservationSerializer(serializers.ModelSerializer):
    book_title = serializers.CharField(source='book.title', read_only=True)
    user_name = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Reservation
        fields = '__all__'
    
    def get_book(self, obj):
        return {
            "id": obj.book.id,
            "title": obj.book.title,
            "author": obj.book.author
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff', 'is_superuser']

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
        )
        return user

class BorrowSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)  # or .get_full_name if you use full name
    book = serializers.CharField(source='book.title', read_only=True)

    class Meta:
        model = Borrow
        fields = ['id', 'borrow_date', 'return_date', 'user', 'book']

class BorrowCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = '__all__'

    def validate(self, data):
        book = data.get('book')
        if not book.available:
            raise serializers.ValidationError("Book is not available for borrowing.")
        return data

