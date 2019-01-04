from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse

from .models import Answer, QuestionReal


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
