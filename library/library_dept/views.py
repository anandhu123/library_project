from django.shortcuts import render
from library_dept.models import *
from library_dept.serializers import *
from rest_framework.response import Response
from rest_framework import (filters, generics, pagination, permissions, status,
                            views)
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class BooksView(generics.ListCreateAPIView):
    serializer_class = BooksSerializer
    queryset = Books.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        data_queryset = Books.objects.all()
        return data_queryset

    def post(self, request, format=None):
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            return Response({"Status": status.HTTP_201_CREATED,
                             "Message": "Successfully Created"})
        return Response({"Status": status.HTTP_400_BAD_REQUEST,
                         "Message": serializer.errors})

class BooksDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BooksSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk, format=None):
        try:
            details = Books.objects.get(pk=pk)
        except:
            return Response({'Status': status.HTTP_404_NOT_FOUND,
                             'Message': "Item not found"})
        serializer = BooksSerializer(details)
        return Response({'Status': status.HTTP_200_OK,
                         'Data': serializer.data})

    def put(self, request, pk, format=None):
        try:
            details = Books.objects.get(pk=pk)
        except:
            return Response({'Status': status.HTTP_404_NOT_FOUND,
                             'Message': "Item not found"})

        serializer = BooksSerializer(details, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Status': status.HTTP_204_NO_CONTENT,
                             'Message': "Successfully Updated!"})
        return Response({'Status': status.HTTP_400_BAD_REQUEST,
                         'Message': serializer.errors} )

    def delete(self, request, pk, format=None):
        try:
            details = Books.objects.get(pk=pk)
        except:
            return Response({'Status': status.HTTP_404_NOT_FOUND,
                             'Message': "Item not found"})
        try:
            details.delete()
            return Response({'Status': status.HTTP_204_NO_CONTENT,
                             'Message': "Successfully Deleted!"})
        except:
            return Response({'Status': status.HTTP_400_BAD_REQUEST,
                             'Message': "Deletion failed!"})

class BorrowView(generics.ListCreateAPIView):
    serializer_class = BorrowSerializer
    queryset = BorrowBooks.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        data_queryset = BorrowBooks.objects.all()
        return data_queryset

    def post(self, request, format=None):
        serializer = BorrowSerializer(data=request.data)
        obj = Books.objects.get(id=request.data['book'])
        if obj.count == 0:
            return Response({"Status":status.HTTP_404_NOT_FOUND,
                             "Message": "Item Unavaibale"})
        if serializer.is_valid():
            serializer.save()
            obj.count = obj.count - 1
            obj.save()
            return Response({"Status": status.HTTP_201_CREATED,
                             "Message": "Successfully Created"})
        return Response({"Status":status.HTTP_400_BAD_REQUEST
                            , "Message": serializer.errors})

class UserBorrowBooksView(generics.RetrieveAPIView):
    serializer_class = BorrowDetailsSerializer
    queryset = BorrowBooks.objects.all()
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk, format=None):
        try:
            details = BorrowBooks.objects.filter(user=pk)
        except:
            return Response({'Status':status.HTTP_404_NOT_FOUND,
                             'Message': "Item not found"})
        serializer = BorrowDetailsSerializer(details, many=True)
        return Response({'Status': status.HTTP_200_OK,
                         'Data': serializer.data})