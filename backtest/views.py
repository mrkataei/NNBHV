from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .strategy_tester import StrategyTaster
from . import serializers
from strategy.models import Strategies


@api_view(['GET'])
@permission_classes((AllowAny, ))
def backtest(request):
    try:
        Strategies.objects.get(name=request.query_params['name'])
        return Response('slama', status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
