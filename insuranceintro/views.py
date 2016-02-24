from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import View

# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request, "index.html")

class ElementView(View):
    def get(self, request):
        return render(request, "elements.html")

class QuestionView(View):
    def get(self, request):
        return render(request, "questions.html")