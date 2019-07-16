from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.
def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    output = ", ".join(q.question_text for q in latest_questions)
    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse("This is the detailed view of the question: {}".format(question_id))

def results(request, question_id):
    return HttpResponse("These are the results of the question: {}".format(question_id))

def vote(request, question_id):
    return HttpResponse("Votes for question: {}".format(question_id))