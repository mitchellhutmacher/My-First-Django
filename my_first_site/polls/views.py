from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello, world.  You're at the polls index.  ")


def detail(request, question_id):
    """
    Show the question ID
    """
    resp = "You're looking at question {0}.".format(question_id)
    return HttpResponse(resp)


def results(request, question_id):
    resp = "You're looking at the results of question {0}.".format(question_id)
    return HttpResponse(resp)


def vote(request, question_id):
    resp = "You're voting on question {0}.".format(question_id)
    return HttpResponse(resp)
