from asyncore import read
from unicodedata import category
from rest_framework.serializers import ModelSerializer
from products.models import Product
from categories.Api.serializers import CategorySerializer

class ProductSerializer(ModelSerializer):

    category_data = CategorySerializer(source = 'category', read_only = True)

    class Meta:
        model = Product
        fields = ['id','title','image', 'price', 'active', 'category', 'category_data']