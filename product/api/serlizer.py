from ..models import *
from rest_framework import serializers
from django.shortcuts import get_object_or_404

# serializers.py
from rest_framework import serializers
from ..models import Product, Category

class CategorySerlizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerlizer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerlizer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        try:
            category_id = validated_data.pop('category_id')
            category = Category.objects.get(pk=category_id)
            return Product.objects.create(category=category, **validated_data)
        except Category.DoesNotExist:
            raise serializers.ValidationError(
                {"category_id": "Invalid category ID"}
            )

    def update(self, instance, validated_data):
        category_id = validated_data.pop('category_id', None)
        if category_id:
            category = get_object_or_404(Category, pk=category_id)
            instance.category = category
        return super().update(instance, validated_data)


