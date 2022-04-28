from rest_framework import viewsets
from . import models
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Prefetch


class FoodViewSet(viewsets.ModelViewSet):
    queryset = models.FoodCategory.objects.all()
    serializer_class = models.FoodListSerializer
    http_method_names = ['get']
    @action(detail=False, methods=['GET'])
    def food(self, request):
        queryset = models.FoodCategory.objects.prefetch_related(Prefetch(
            'food',
            queryset=models.Food.objects.filter(is_publish=True))).order_by('order_id')
        serializer = models.FoodListSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
