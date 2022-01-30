from rest_framework.views import APIView
from .models import *
from .serializers import AnswerSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction

# Create your views here.

class MyApi(APIView):

    @transaction.atomic
    def post(self, request):
        answers = request.data.get('answers', [])
        if len(answers) == 0:
            return Response({'detail': "Ответ не может быть пустым"}, status.HTTP_400_BAD_REQUEST)

        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            quiz = Quiz(
                first_name=serializer.validated_data.get('first_name', ''),
                last_name=serializer.validated_data.get('last_name', ''),
                phone=serializer.validated_data.get('phone', ''),
                email=serializer.validated_data.get('email', ''),
                age=serializer.validated_data.get('age', ''),
                country=serializer.validated_data.get('country', ''),
                res1=serializer.validated_data.get('results').get('res1'),
                res2=serializer.validated_data.get('results').get('res2'),
                res3=serializer.validated_data.get('results').get('res3'),
                res4=serializer.validated_data.get('results').get('res4'),
                res5=serializer.validated_data.get('results').get('res5'),
                res6=serializer.validated_data.get('results').get('res6'),
                res7=serializer.validated_data.get('results').get('res7'),

            )
            quiz.save()
            for answer in answers:
                ua = Answer(
                    quiz=quiz,
                    answerId=answer['answerId'],
                    questionId=answer['questionId'],
                    questionText=answer['questionText'],
                    answerText=answer['answerText']
                )
                ua.save()

            return Response({'detail': 'Успешно создан'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

