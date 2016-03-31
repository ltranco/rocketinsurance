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

class TermView(View):
    def get(self, request):
        return render(request, "term.html")

class PermView(View):
    def get(self, request):
        return render(request, "perm.html")

class ContactView(View):
    def get(self, request):
        return render(request, "contact.html")