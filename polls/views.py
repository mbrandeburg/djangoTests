from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
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
    ## original:
    # return HttpResponse("This is the detailed view of the question: {}".format(question_id))
    
    ## revisied:
    question = get_object_or_404(Question, pk=question_id)
    # wont pass in variabvle with dictionary this time..just gunna code the dictionary inside
    return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
    # return HttpResponse("These are the results of the question: {}".format(question_id))
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/results.html', {'question':question})

def vote(request, question_id):
    # return HttpResponse("Votes for question: {}".format(question_id))

    # now let's write the python logic to store choices, etc., from the voting app
    question = get_object_or_404(Question, pk=question_id)
    try:
        # use post to get a dictionary that gets us back the id which is what pk takes!
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except:
        return render(request, 'polls/detail.html', {'question': question, 'error_message': 'Please select a choice!'})
    else:
        # so you've voted, so lets increment and save and redirect to your results!
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id)))