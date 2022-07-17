from django.shortcuts import render
from django.http import HttpResponse

from .models import Question


def index(request):
    """
    Show the 5 most recent questions
    """
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list
    }
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    """
    Show the question ID
    """
    resp = "You're looking at question {0}.".format(question_id)
    return HttpResponse(resp)


def results(request, question_id):
    """
    Show the results of the question
    """
    resp = "You're looking at the results of question {0}.".format(question_id)
    return HttpResponse(resp)


def vote(request, question_id):
    """
    Vote on the question
    """
    resp = "You're voting on question {0}.".format(question_id)
    return HttpResponse(resp)
