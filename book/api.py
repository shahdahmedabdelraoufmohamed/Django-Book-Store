from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Category, Book
from .serializer import CategorySerializer, BookSerializer
from users.models import CustomPublisher
from rest_framework.pagination import PageNumberPagination


class CategoryListApi(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # lookup_field = 'slug'


class CategoryDetailsApi(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryCreateApi(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryUpdateApi(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDeleteApi(generics.DestroyAPIView):
    queryset = Category.objects.all()

class BookListApi(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def book_details(request, id):
    book = Book.objects.get(id=id)
    data = BookSerializer(book, context={'request':request}).data
    return Response({'book':data})
 

def book_details_by_publisher(request, id):
    book = Book.objects.get(id=id)
    if request.user.id == book.publisher_id:
        data = BookSerializer(book, context={'request':request}).data
        return Response({'book':data})
    else:
        return Response({"Erorr": "You are not the book Publisher"})


class BookCreateApi(generics.CreateAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        print(self.request.user.id)      
        publisher = CustomPublisher.objects.get(id = self.request.user.id)
        serializer.save(publisher=publisher) 

class BookUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    print("called")
    def perform_update(self, serializer):
        print("called second")
        publisher = CustomPublisher.objects.get(id = self.request.user.id)
        serializer.save(publisher=publisher)   
    
    def patch(self, request, *args, **kwargs):
        print(request.data)
        return super().patch(request, *args, **kwargs)


class BookDeleteApi(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_publisher_books(request):
    """Return list of books created by the request publisher"""
    paginator = PageNumberPagination()
    publisher_books = Book.objects.filter(publisher_id = request.user.id)
    result_page = paginator.paginate_queryset(publisher_books, request)
    books_serializer = BookSerializer(result_page, many=True)
    return paginator.get_paginated_response(books_serializer.data)


