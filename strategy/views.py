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


@api_view(['PUT', 'GET', 'DELETE'])
@permission_classes((IsAuthenticated, IsOwner))
def get_update_delete_strategy(request, pk):
    try:
        strategy = UserStrategies.objects.get(pk=pk)
    except:
        return Response({"error": "Not Found!"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        ser = UserStrategySerializer(strategy)
        return Response(ser.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        ser = UserStrategySerializer(strategy, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        strategy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

