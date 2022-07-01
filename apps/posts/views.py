from locale import currency
from django.http import HttpResponse
from django.shortcuts import redirect, render
from apps.posts.models import Post
from apps.settings.models import Setting

# Create your views here.
def post_detail(request, id):
    post = Post.objects.get(id = id)
    setting = Setting.objects.latest('id')
    random_posts = Post.objects.all().order_by('?')
    context = {
        'setting' : setting,
        'post' : post,
        'random_posts' : random_posts,
    }
    return render(request, 'posts/shop-single.html', context)

def post_create(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        # try:
        post_image = request.FILES.get('post_image')
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        currency = request.POST.get('currency')
        phone = request.POST.get('price')
        post = Post.objects.create(user = request.user, title = title, post_image = post_image, description = description, price = price, currency = currency, phone = phone)
        return redirect('index')
        # except:
        #     return HttpResponse("Error")

    context = {
        'setting' : setting,
    }
    return render(request, 'posts/create.html', context)