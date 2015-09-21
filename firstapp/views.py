from django.shortcuts import render
from django.utils import timezone
from datetime import datetime
from .models import Post

def home(request):
  return render(request, "firstapp/home-template.html", {
  'time': datetime.now
  })

def post_list(request):
  posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
  return render(request, "firstapp/home-template.html", {'posts': posts})