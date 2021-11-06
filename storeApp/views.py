import requests

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import StoreOrder
from .serializers import StoreOrderSerializer


@api_view(['POST'])
def store_order_create(request):
    serializer = StoreOrderSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        request.data["store_account"] = serializer.data["id"]
        requests.post('http://127.0.0.1:8002/warehouse-order/create/', data=request.data)
    else:
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PATCH'])
def store_order_update(request, pk):
    required_store_order = StoreOrder.objects.get(order_number=pk)
    serializer = StoreOrderSerializer(instance=required_store_order, data=request.data)

    if serializer.is_valid():
        serializer.save()

        request.data["store_account"] = serializer.data["id"]
        requests.patch('http://127.0.0.1:8002/warehouse-order/update-from-store/{0}/'.format(pk), data=request.data)
    else:
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PATCH'])
def store_order_update_from_warehouse(request, pk):
    required_store_order = StoreOrder.objects.get(order_number=pk)
    serializer = StoreOrderSerializer(instance=required_store_order, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def store_order_delete(request, pk):
    required_store_order = StoreOrder.objects.get(order_number=pk)
    required_store_order.delete()

    requests.delete('http://127.0.0.1:8002/warehouse-order/delete/{0}/'.format(pk))

    return Response('Store Order and Warehouse Order were successfully deleted', status=status.HTTP_200_OK)


@api_view(['GET'])
def store_order_detail(request, pk):
    store_order = StoreOrder.objects.get(id=pk)
    serializer = StoreOrderSerializer(store_order, many=False)

    return Response(serializer.data, status=status.HTTP_200_OK)
