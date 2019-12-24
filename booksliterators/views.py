from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import VoteSerializer, BookDetailSerializer, LiteratorDetailSerializer, BookListSerializer, LiteratorListSerializer
from .models import Vote, Book, Literator
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Max, Avg


class VoteForBook(APIView):
    '''
    Оценивает книгу
    '''

    def post(self, request, pk):
        serializer = VoteSerializer(data=self.request.data)
        if serializer.is_valid():
            vote = Vote.objects.create(value=serializer.validated_data['value'],
                                       book_id=pk)
            vote.save()  # сохраняем в бд

            book = Book.objects.get(pk=pk)
            all_votes = book.votes.all()  # Выбираем все голоса к данной книге
            average_rating = all_votes.aggregate(average_value=Avg('value'))  # вычисляем среднее значение
            book.rating = average_rating['average_value']  # делаем из значения целое число и возращаем
            book.save() # обновляем поле с рейтингом в бд
            print(book.rating)

            return Response(data='You have successfully voted!', status=status.HTTP_201_CREATED)
        else:
            return Response(data='Bad request!', status=status.HTTP_400_BAD_REQUEST)


class BookList(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer




class BookDetail(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer

class LiteratorList(ListCreateAPIView):
    queryset = Literator.objects.all()
    serializer_class = LiteratorListSerializer

class LiteratorDetail(RetrieveUpdateDestroyAPIView):
    queryset = Literator.objects.all()
    serializer_class = LiteratorDetailSerializer