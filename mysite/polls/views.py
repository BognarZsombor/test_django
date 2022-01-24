from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

def index(request):
    if request.method == 'GET':
        question_filter = request.GET.get('search')
        if question_filter is None:
            question_list = Question.objects.filter(end_date__gte=timezone.now()).filter(pub_date__lte=timezone.now()).order_by('-end_date')
            context = { 'question_list': question_list }

            return render(request, 'polls/index.html', context)
        
        question_list = Question.objects.filter(question_text__icontains=question_filter).filter(end_date__gte=timezone.now()).filter(pub_date__lte=timezone.now()).order_by('-end_date')
        context = { 'question_list': question_list }

        return render(request, 'polls/index.html', context)
    else:
        search_result = Question.objects.filter(end_date__gte=timezone.now()).filter(pub_date__lte=timezone.now()).order_by('-end_date')
        context = { 'question_list': question_list }

        return render(request, 'polls/index.html', context)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/vote.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:detail', args=(question.id,)))