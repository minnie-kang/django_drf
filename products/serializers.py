from rest_framework import serializers
from .models import Product


class ProductListSerializer(serializers.ModelSerializer):
    """게시글 목록 죄회 Serializer"""
    author = serializers.ReadOnlyField(source='author.email') # author 필드에 작성자의 이메일만 출력

    class Meta:
        model = Product
        fields = ('id', 'author', 'title', 'created_at')
        
        
class ProductDetailSerializer(serializers.ModelSerializer):
    """게시글 상세 조회 및 생성 Serializer"""
    author = serializers.ReadOnlyField(source='author.email') # author 필드에 작성자의 이메일만 출력
    
    class Meta:
        model = Product
        fields = ('id', 'author', 'title', 'content', 'created_at', 'updated_at',)