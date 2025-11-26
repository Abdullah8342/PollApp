from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render,get_object_or_404
from .models import Question,Choice
from django.template import loader
from django.views import generic



class IndexView(generic.ListView):
    template_name = "poll/index.html"
    context_object_name = 'latest_question_list'
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    def get_queryset(self):
        return Question.objects.all()

class DetailView(generic.DetailView):
    model = Question
    template_name = 'poll/details.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'poll/result.html'



def vote(request,question_id):
    question = get_object_or_404(Question,id = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(
            request,
            'poll/details.html',
            {
                'question':question,
                'error_message':'Choice Does Not Selected'
            }
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results',args=(question.id,)))
