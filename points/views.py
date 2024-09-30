from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Points
from rest_framework import status
from django.db.models import Sum
from .serializers import PointsSerializer

@api_view(['POST'])
def add(request):
    serializer = PointsSerializer(data = request.data)
    if serializer.is_valid():
        payer = serializer.validated_data['payer']
        points = serializer.validated_data['points']
        timestamp = serializer.validated_data['timestamp']
        # If trying to add negative points
        if points < 0:
            # Get the sum of all points from the same payer
            current_balance = Points.objects.filter(payer=payer).aggregate(Sum('points'))['points__sum'] or 0
            # If there is not enough points from the payer then return not enough points
            if current_balance + points < 0:
                return Response("Not enough points for this payer", status=status.HTTP_400_BAD_REQUEST)
        Points.objects.create(payer=payer, points=points, timestamp=timestamp)
        return Response(status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def spend(request):
    spending = request.data.get('points')
    deductions = {}
    final_deductions = []
    # Get all points from the account
    total_points = Points.objects.aggregate(total_points=Sum('points'))['total_points'] or 0
    # If trying to spend more points than the account has, return not enough points
    if total_points < spending:
        return Response('Not enough points',status=status.HTTP_400_BAD_REQUEST)
    
    transactions = Points.objects.order_by('timestamp')
    for transaction in transactions:
        
        # Check how many points are available to deduct from this transaction
        points_to_deduct = min(spending, transaction.points)

        # Deduct points from this transaction
        spending -= points_to_deduct
        transaction.points -= points_to_deduct
        transaction.save()
        deductions[transaction.payer] =  deductions.get(transaction.payer, 0) + (-points_to_deduct)

        if spending == 0:
            break
        
    for payer, points in deductions.items():
        final_deductions.append({'payer' : payer , 'points' : points})
    return Response(final_deductions, status=status.HTTP_200_OK)

@api_view(['GET'])
def balance(request):
    transactions = Points.objects.values('payer').annotate(total_points=Sum('points'))
    response = {}
    for transaction in transactions:
        response[transaction['payer']] = transaction['total_points']
    return Response(response,status=status.HTTP_200_OK)