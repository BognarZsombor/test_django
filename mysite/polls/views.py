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
        # Filtering question_list with search bar
        # 'search' 'question_list'
        question_filter = request.GET.get('search')
        if question_filter is None:
            question_list = Question.objects.filter(end_date__gte=timezone.now()).filter(pub_date__lte=timezone.now()).order_by('-end_date')
            context = { 'question_list': question_list }

            return render(request, 'polls/index.html', context)
        
        question_list = Question.objects.filter(question_text__icontains=question_filter).filter(end_date__gte=timezone.now()).filter(pub_date__lte=timezone.now()).order_by('-end_date')
        context = { 'question_list': question_list }

        return render(request, 'polls/index.html', context)
    elif request.method == 'POST':
        # Adding new question to the database
        # 'question_text' 'pub_date' 'end_date'
        question_text = request.POST.get('question_text')
        pub_date = request.POST.get('pub_date')
        end_date = request.POST.get('end_date')
        print(pub_date)
        print(end_date)
        if question_text and pub_date != "" and end_date != "":
            question = Question(question_text=question_text, pub_date=pub_date, end_date=end_date)
            question.save()
            return HttpResponseRedirect(reverse('polls:index'))
        elif pub_date == "" and end_date == "":
            question = Question(question_text=question_text)
            question.save()
            return HttpResponseRedirect(reverse('polls:index'))
        elif pub_date == "":
            question = Question(question_text=question_text, end_date=end_date)
            question.save()
            return HttpResponseRedirect(reverse('polls:index'))
        elif end_date == "":
            question = Question(question_text=question_text, pub_date=pub_date)
            question.save()
            return HttpResponseRedirect(reverse('polls:index'))
        else:
            return render(request, 'polls/index.html', {
                'error_message': "Error, your question wasn't posted."
            })
    else:
        search_result = Question.objects.filter(end_date__gte=timezone.now()).filter(pub_date__lte=timezone.now()).order_by('-end_date')
        context = { 'question_list': question_list }

        return render(request, 'polls/index.html', context)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.POST.get('choice'):
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
    elif request.POST.get('choice_text'):
        choice_text = request.POST.get('choice_text')
        if choice_text:
            question.choice_set.create(choice_text=choice_text)
            return HttpResponseRedirect(reverse('polls:vote', args=(question.id,)))
        else:
            return render(request, 'polls/vote.html', {
                'error_message': "Error, your choice wasn't posted."
            })
    else:
        return render(request, 'polls/vote.html', {
            'question': question,
        })
