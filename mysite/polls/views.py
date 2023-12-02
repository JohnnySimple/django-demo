from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

def index(request):
    return HttpResponse("You know how we do it. Let's go to the mars🚀")


def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    return HttpResponse("You are looking at question %s." % question)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
