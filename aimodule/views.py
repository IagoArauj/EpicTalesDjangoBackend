from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from .models import AIModel
from .aibuilder import AIBuilder

@api_view(['POST'])
def generate_response(request: Request) -> Response:
    if request.method == 'POST':
        user_input = request.data.get('user_input', '')
        temperature = request.data.get('temperature', 0.5)
        model_name = request.data.get('model_name', 'llama3-70b-8192')
        
        if not user_input:
            return Response({'response': 'User input is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        print(f"User input: {user_input} | Temperature: {temperature} | Model: {model_name}")
        
        try:
          response = AIBuilder.get_response(model=model_name, temperature=temperature, input=user_input)
        except Exception as e:
          print(f"Error: {e}")
          return Response({'response': 'INTERNAL_SERVER_ERROR'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        ai_model = AIModel.objects.create(
            user_input=user_input,
            response=response,
            temperature=temperature,
            model_name=model_name
        )
        print(f"{ai_model.user_input} -> {ai_model.response}")
        
        ai_model.save()
        return Response({'response': response}, status=status.HTTP_200_OK)
    return Response({'response': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)