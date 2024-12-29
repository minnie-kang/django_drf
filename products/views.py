# articles/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductListSerializer, ProductDetailSerializer

class ProductListCreate(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        """상품 목록 조회"""
        products = Product.objects.all()
        serializer = ProductListSerializer(products, many=True)  # 목록용 Serializer 사용
        return Response(serializer.data)

    def post(self, request):
        """상품 생성"""
        serializer = ProductDetailSerializer(data=request.data)  # 상세 Serializer 사용
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, product_pk):
        return get_object_or_404(Product, pk=product_pk)

    def get(self, request, product_pk):
        """상품 상세 조회"""
        product = self.get_object(product_pk)
        serializer = ProductDetailSerializer(product)  # 상세 Serializer 사용
        return Response(serializer.data)

    def put(self, request, product_pk):
        """상품 수정"""
        product = self.get_object(product_pk)
        if product.author != request.user:
            return Response({"detail": "수정 권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = ProductDetailSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, product_pk):
        """상품 삭제"""
        product = self.get_object(product_pk)
        if product.author != request.user:
            return Response({"detail": "삭제 권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)
        
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)