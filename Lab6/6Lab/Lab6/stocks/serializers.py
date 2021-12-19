from .models import Stock
from rest_framework import serializers



class StockSerializer(serializers.ModelSerializer):
    class Meta:

        model = Stock

        fields = ["pk", "company_name", "price", "is_growing", "date_modified"]

