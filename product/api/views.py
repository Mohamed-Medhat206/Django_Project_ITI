from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status,viewsets
from django.shortcuts import get_object_or_404
from .serlizer import ProductSerlizer
from ..models import Product
from rest_framework.views import APIView
from rest_framework import generics



class ProductViewSet(viewsets.ViewSet):
    
    def list(self, request):
        products = Product.getall()
        serializer = ProductSerlizer(products, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = ProductSerlizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerlizer(product)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerlizer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        """Partial update of a product"""
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerlizer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        product.softdelete(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerlizer
    lookup_field = 'pk'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.softdelete()
        return Response(
            {"message": "Product deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerlizer


class ProductUpdateAPIView(APIView):
    def put(self, request, pk):
        try:
            product = get_object_or_404(Product, pk=pk)
            serializer = ProductSerlizer(product, data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "Product updated successfully"},
                    status=status.HTTP_200_OK
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    # Add this to handle PATCH requests as well if needed
    def patch(self, request, pk):
        return self.put(request, pk)




@api_view(['GET', 'DELETE'])
def getbyid(request, id):
    product = get_object_or_404(Product, pk=id)

    if request.method == 'GET':
        serialized = ProductSerlizer(product)
        return Response(serialized.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        try:
            product.softdelete(id) 
            return Response({"message": "Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])  
def getallpro(request):
    if request.method == 'GET':
        products = Product.getall()
        P_After_serializer = ProductSerlizer(products, many=True)
        return Response(P_After_serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        print("Request data:", request.data)
        serializer = ProductSerlizer(data=request.data)
        if serializer.is_valid():
            print("Serializer is valid. Saving...")
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            print("Serializer errors:", serializer.errors) 
            return Response(serializer.errors, status=400)
    
