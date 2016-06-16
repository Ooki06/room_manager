import sqlite3
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'room_manager/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'room_manager/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'room_manager/results.html'

class YoyakuView(generic.ListView):
    model = Question
    template_name = 'room_manager/yoyaku.html'

class TableView(generic.ListView):
    model = Question
    conn = sqlite3.connect('./db.sqlite3')
    cur = conn.cursor()
    cur.execute("""SELECT * FROM room;""")
    template_name = 'room_manager/table.html'

class YoyakudelView(generic.ListView):
    model = Question
    template_name = 'room_manager/yoyakudel.html'

class ZikanwariView(generic.ListView):
    model = Question
    template_name = 'room_manager/zikanwari.html'

class LoginView(generic.ListView):
    model = Question
    template_name = 'room_manager/login.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'room_manager/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('room_manager:results', args=(question.id,)))

