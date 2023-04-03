from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt

from .models import Product
from .serializers import ProductSerializer

# Create your views here.
class AllView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
class ViewView(APIView):
    def get(self, request, id):

        product = Product.objects.filter(id=id).first()

        if product is None:
            return Response({
                "message" : "Product Not Found!"
            })
        
        serializer = ProductSerializer(product)
        return Response(serializer.data)
        

class AddView(APIView):
    def post(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class UpdateView(APIView):
    def put(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        
        id = request.data['id']
        product = Product.objects.filter(id=id).first()

        if product is None:
            return Response({
                "message" : "Product Not Found!"
            })
        
        serializer = ProductSerializer(product, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class DeleteView(APIView):
    def delete(self, request, id):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        product = Product.objects.filter(id=id).first()

        if product is None:
            return Response({
                "message" : "Product Not Found!"
            })
        
        product.delete()
        return Response({
                "message" : id + " deleted successfully!"
            })