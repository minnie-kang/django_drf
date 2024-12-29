from rest_framework import serializers
from .models import Product

# 상품 목록 조회 Serializer
class ProductListSerializer(serializers.ModelSerializer):
    """상품 목록 죄회 Serializer"""

    class Meta:
        model = Product
        fields = ('id', 'author', 'title', 'created_at', 'view_count')  # 조회수 필드 추가
        read_only_fields = ('author', )
        
        
class ProductDetailSerializer(serializers.ModelSerializer):
    """상품 상세 조회 및 생성 Serializer"""
    author = serializers.ReadOnlyField(source='author.email') # author 필드에 작성자의 이메일만 출력
    
    class Meta:
        model = Product
        fields = ('id', 'author', 'title', 'content', 'created_at', 'updated_at', 'view_count')  # 조회수 필드 추가

