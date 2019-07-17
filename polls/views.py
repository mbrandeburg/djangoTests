from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# from django.template import loader, RequestContext # no longer needed after `revised - simplified` under index

# Create your views here.
def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    ## original way:
    # output = ", ".join(q.question_text for q in latest_questions)
    # return HttpResponse(output)
    
    #### revised:
    ## in {}: passing a dictionary here of what we are passing, like leaderboard into jinja variables in index.html
    # context = RequestContext(request, {
    #     'latest_questions':latest_questions
    #     })
    # context_dict = context.flatten() #turn it into the dictionary
    # template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render(context_dict))

    #### revised - simplified:
    context = {'latest_questions':latest_questions}
    return render(request,'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse("This is the detailed view of the question: {}".format(question_id))

def results(request, question_id):
    return HttpResponse("These are the results of the question: {}".format(question_id))

def vote(request, question_id):
    return HttpResponse("Votes for question: {}".format(question_id))