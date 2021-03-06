from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

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
    Show the question ID, 404 if there is an invalid question ID
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


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
