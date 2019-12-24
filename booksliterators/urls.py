from django.conf.urls import url, include
from .views import LiteratorList, LiteratorDetail, BookList, BookDetail, VoteForBook

urlpatterns = [
    url(r'^literators/(?P<pk>\d+)/', LiteratorDetail.as_view()),
    url(r'^literators/', LiteratorList.as_view()),
    url(r'^books/(?P<pk>\d+)/vote/$', VoteForBook.as_view()),
    url(r'^books/(?P<pk>\d+)/$', BookDetail.as_view()),
    url(r'^books/$', BookList.as_view()),


]
