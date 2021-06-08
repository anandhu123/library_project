from rest_framework import serializers
from library_dept.models import *
from authentication.serializers import *

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowBooks
        fields = '__all__'


class BorrowDetailsSerializer(serializers.ModelSerializer):
    book = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    def get_book(self, obj):
        return BooksSerializer(obj.book).data

    def get_user(self, obj):
        return UserDetailSerializer(obj.user).data

    class Meta:
        model = BorrowBooks
        fields = ('id', 'book', 'user', 'timestamp', 'returned', 'returned_date')