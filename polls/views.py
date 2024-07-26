from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.db.models import F

from .models import Question, Choice


# Create your views here.
def index(request):
    list_latest_questions = Question.objects.order_by("-publish_date")[0:5]
    # template = loader.get_template("polls/index.html")
    context = {
        "list_latest_questions": list_latest_questions
    }
    # return HttpResponse(template.render(context, request))
    return render(request, "polls/index.html", context)



def detail(request, question_id):
    try:
        question = get_object_or_404(Question, pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})


from django.shortcuts import get_object_or_404, render


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))