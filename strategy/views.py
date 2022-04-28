from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from user.permissions import IsOwner
from .models import UserStrategies
from .serializers import UserStrategySerializer


@api_view(['GET'])
@permission_classes((IsAuthenticated, IsOwner))
def strategies(request):
    try:
        strategy = UserStrategies.objects.filter(user=request.query_params['username'])
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    ser = UserStrategySerializer(strategy, many=True)
    return Response(ser.data, status=status.HTTP_200_OK)
