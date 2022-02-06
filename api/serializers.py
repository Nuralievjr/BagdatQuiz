from rest_framework import serializers
from .models import *
class ARR(serializers.Serializer):
    answerId = serializers.IntegerField(required=True)
    questionId = serializers.IntegerField(required=True)
    questionText = serializers.CharField(required=True)
    answerText = serializers.CharField(required=True)

class Res(serializers.Serializer):
    res1 = serializers.CharField(required=True)
    res2 = serializers.CharField(required=True)
    res3 = serializers.CharField(required=True)
    res4 = serializers.CharField(required=True)
    res5 = serializers.CharField(required=True)
    res6 = serializers.CharField(required=True)
    res7 = serializers.CharField(required=True)

class AnswerSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    age = serializers.CharField(required=True)
    country = serializers.CharField(required=True)
    is_parent = serializers.BooleanField(required=True)
    answers = ARR(required=True, many=True)
    results = Res(required=True, many=False)


