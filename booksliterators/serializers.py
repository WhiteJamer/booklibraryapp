from rest_framework import serializers, pagination
from .models import Vote, Book, Literator
from django.db.models import Max, Avg


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['value', 'book']


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['pk', 'name', 'literators', 'rating']


class BookDetailSerializer(serializers.ModelSerializer):
    literators = serializers.StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = ['pk', 'name', 'literators', 'rating']


class BookTopRatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['pk', 'rating']


class LiteratorListSerializer(serializers.ModelSerializer):
    books = serializers.SerializerMethodField('top_rated_books')

    class Meta:
        model = Literator
        fields = ['pk', 'name', 'books']

    def top_rated_books(self, obj):
        books = obj.books.all().order_by('-rating')[:5]  # 5 книг по рейтингу
        serializer = BookTopRatedSerializer(books, many=True)
        return serializer.data


class LiteratorDetailSerializer(serializers.ModelSerializer):
    books = serializers.SerializerMethodField('top_rated_books')

    class Meta:
        model = Literator
        fields = ['pk', 'name', 'books']

    def top_rated_books(self, obj):
        books = obj.books.all().order_by('-rating')[:5]  # 5 книг по рейтингу
        serializer = BookTopRatedSerializer(books, many=True)
        return serializer.data
