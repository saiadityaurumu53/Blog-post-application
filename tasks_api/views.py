from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer



class AddNumberView(APIView):
    """
    API view to add 2 numbers
    """
    def post(self, request, *args, **kwargs):
        #now we need to extract the numbers from the request data
        try:
            num1 = request.data.get('num1', None)
            num2 = request.data.get('num2', None)

            if (num1 is None) or (num2 is None):
                return Response({"error": "Please provide both num1 and num2"}, status=status.HTTP_400_BAD_REQUEST)
            
            #now we need to ensure both the number inputs are float
            num1 = float(num1)
            num2 = float(num2)

            # perform addition
            result = num1 + num2

            return Response({"result" : result}, status=status.HTTP_200_OK)
        
        except ValueError:
            return Response({"error": "Invalid input. Please provide valid numbers."}, status=status.HTTP_400_BAD_REQUEST)


