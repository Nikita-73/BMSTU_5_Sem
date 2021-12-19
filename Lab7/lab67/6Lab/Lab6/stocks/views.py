from rest_framework import viewsets
from .serializers import StockSerializer
from .models import Stock


class StockViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Stock.objects.all().order_by('id')
    serializer_class = StockSerializer

