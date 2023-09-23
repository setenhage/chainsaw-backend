from django.shortcuts import get_object_or_404
from django.http.response import JsonResponse

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from apps.address.serializers import AddressSerializer
from public.models import Address

@api_view(['GET'])
def address_view(request, pk=None):
    if pk:
        serializer = AddressSerializer(get_object_or_404(Address, id=pk))
        data = {
            'object': serializer.data
        }
        return Response(data)

@api_view(['POST'])
def address_create(request):
    print('request', request.data)
    serializer = AddressSerializer(data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)