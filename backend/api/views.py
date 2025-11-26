from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MenuItem, Order
from .serializers import MenuSerializer, OrderSerializer
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def signup_user(request):
    name = request.data.get("name")
    email = request.data.get("email")
    password = request.data.get("password")

    # 1. Check if email already registered
    if User.objects.filter(username=email).exists():
        return Response({"success": False, "message": "Email already exists"}, status=400)

    # 2. Create user
    user = User.objects.create_user(
        username=email,
        email=email,
        password=password,
        first_name=name
    )

    return Response({"success": True, "message": "Signup successful"})


@api_view(['POST'])
def login_user(request):
    email = request.data.get("email")
    password = request.data.get("password")

    user = authenticate(username=email, password=password)

    if user is not None:
        return Response({"success": True, "message": "Login successful"})
    else:
        return Response({"success": False, "message": "Invalid email or password"}, status=400)


def home(request):
    return redirect('/menu')


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
