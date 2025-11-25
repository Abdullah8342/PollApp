from django.http import HttpResponse,Http404
from django.urls import reverse
from django.shortcuts import render,get_object_or_404
from .models import Question,Choice
from django.template import loader



def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list}
    other_url = reverse('index')
    print(other_url)
    return render(request,'poll/index.html',context)


def detail(request,question_id):
    question = get_object_or_404(Question,id = question_id)
    context = {'question':question}
    return render(request,'poll/details.html',context)


def results(request,question_id):
    return HttpResponse(f'Your Are Looking At Result {question_id}')

def vote(request,question_id):
    return HttpResponse(f'You Are Looking At Vote {question_id}')
