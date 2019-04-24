from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Question
from django.core import serializers


def index(request):
    data = serializers.serialize("json", Question.objects.all())
    return HttpResponse(data)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    data = {
        'question_id': question_id,
        'question_text': question.question_text,
        'pub_date': question.pub_date
    }

    return JsonResponse(data)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
# Create your views here.
