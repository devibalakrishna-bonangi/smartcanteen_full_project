from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MenuItem, Order
from .serializers import MenuSerializer, OrderSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def get_menu(request):
    items = MenuItem.objects.all()
    serializer = MenuSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['PATCH'])
def update_availability(request, id):
    item = get_object_or_404(MenuItem, id=id)
    item.available = request.data.get('available', item.available)
    item.save()
    return Response({'success': True})

@api_view(['POST'])
def place_order(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'success': True, 'orderId': serializer.data.get('id')})
    return Response(serializer.errors, status=400)
