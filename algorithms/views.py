from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .algorithms import binary_search, quick_sort, bfs
from .models import AlgorithmLog


from rest_framework.generics import ListAPIView
from .models import AlgorithmLog
from .serializers import AlgorithmLogSerializer

class AlgorithmLogListView(ListAPIView):
    queryset = AlgorithmLog.objects.all()
    serializer_class = AlgorithmLogSerializer


@api_view(['POST'])
def binary_search_view(request):
    try:
        data = request.data
        arr = data.get('array', [])
        target = data.get('target')
        result = binary_search(arr, target)
        log_call('Binary Search', data, result)
        return Response({'result': result})
    except ValueError as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def quick_sort_view(request):
    try:
        data = request.data
        arr = data.get('array', [])
        result = quick_sort(arr)
        log_call('Quick Sort', data, result)
        return Response({'result': result})
    except ValueError as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def bfs_view(request):
    try:
        data = request.data
        graph = data.get('graph', {})
        start = data.get('start')
        result = bfs(graph, start)
        log_call('BFS', data, result)
        return Response({'result': result})
    except ValueError as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

def log_call(algorithm_name, input_data, output_data):
    AlgorithmLog.objects.create(
        algorithm_name=algorithm_name,
        input_data=input_data,
        output_data=output_data
    )