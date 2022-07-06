from django.shortcuts import render
from apps.settings.models import Setting
from apps.posts.models import Post

# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    posts = Post.objects.all().order_by('?')
    context = {
        'setting' : setting,
        'posts' : posts,
    }
    return render(request, 'index.html', context)