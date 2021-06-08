from django.shortcuts import render
from authentication.models import *
from authentication.serializers import *
from rest_framework.response import Response
from rest_framework import (filters, generics, pagination, permissions, status,
                            views)
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class UserListView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        data_queryset = User.objects.all()
        return data_queryset

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            obj.set_password(request.data['password'])
            obj.save()
            return Response({"Status":status.HTTP_201_CREATED,
                             "Message": "Successfully Created",})
        return Response({"Status": status.HTTP_400_BAD_REQUEST,
                         "Message": serializer.errors,
                         })