from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from pharma.models import Cure
from .serializers import CureSerializer


class CureList(APIView):
    def get(self, request):
        cures = Cure.objects.all()
        serializer = CureSerializer(cures, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CureSerializer(data=request.data)
        if serializer.is_valid():
            title = serializer.validated_data.get('title')
            if Cure.objects.filter(title=title).exists():
                return Response('Такое лекарство уже есть в вашей базе данных', status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CureDetail(APIView):
    def get_object(self, id):
        return get_object_or_404(Cure, id=id)

    def get(self, request, id):
        cure = self.get_object(id)
        serializer = CureSerializer(cure)
        return Response(serializer.data)

    def put(self, request, id):
        cure = self.get_object(id)
        serializer = CureSerializer(cure, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            cure = Cure.objects.get(id=id)
        except Cure.DoesNotExist:
            return Response('Такого лекарства нет!', status=status.HTTP_404_NOT_FOUND)

        cure.is_deleted = True
        cure.save()

        return Response('Лекарство успешно удалено.', status=status.HTTP_204_NO_CONTENT)


class CureDetailWithDetails(APIView):
    def get_object(self, id):
        return get_object_or_404(Cure, id=id)

    def get(self, request, id):
        cure = self.get_object(id)
        serializer = CureSerializer(cure)
        return Response(serializer.data)
