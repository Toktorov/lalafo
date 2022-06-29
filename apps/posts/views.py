from django.shortcuts import render
from apps.posts.models import Post
from apps.settings.models import Setting

# Create your views here.
def post_detail(request, id):
    post = Post.objects.get(id = id)
    setting = Setting.objects.latest('id')
    context = {
        'setting' : setting,
        'post' : post
    }
    return render(request, 'shop-single.html', context)