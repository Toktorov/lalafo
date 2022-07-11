from django.http import HttpResponse
from django.shortcuts import redirect, render
from apps.posts.models import Post, PostImage
from apps.settings.models import Setting
from apps.categories.models import Category
from django.db.models import Q

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
    categories = Category.objects.all()
    if request.method == "POST":
        # try:
        post_image = request.FILES.get('post_image')
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        currency = request.POST.get('currency')
        phone = request.POST.get('price')
        category = request.POST.get('category')
        post = Post.objects.create(user = request.user, title = title, post_image = post_image, description = description, price = price, currency = currency, phone = phone, category_id = category)
        return redirect('index')
        # except:
        #     return HttpResponse("Error")

    context = {
        'setting' : setting,
        'categories' : categories,
    }
    return render(request, 'posts/create.html', context)

def post_update(request, id):
    setting = Setting.objects.latest('id')
    post = Post.objects.get(id = id)
    categories = Category.objects.all()
    if request.method == "POST":
        try:
            post_image = request.FILES.get('post_image')
            title = request.POST.get('title')
            description = request.POST.get('description')
            price = request.POST.get('price')
            currency = request.POST.get('currency')
            phone = request.POST.get('price')
            category = request.POST.get('category')
            post = Post.objects.get(id = id)
            post.post_image = post_image
            post.title = title 
            post.description = description
            post.price = price 
            post.currency = currency
            post.phone = phone 
            post.category_id = category
            post.save()
            return redirect('post_detail', post.id)
        except:
            return HttpResponse("Error")
    context = {
        'setting' : setting,
        'categories' : categories,
        'post' : post,
    }
    return render(request, 'posts/update.html', context)

def post_delete(request, id):
    setting = Setting.objects.latest('id')
    post = Post.objects.get(id = id)
    if request.method == "POST":
        post = Post.objects.get(id = id)
        post.delete()
        return redirect('index')
    context = {
        'setting' : setting,
        'post' : post,
    }
    return render(request, 'posts/delete.html', context)

def post_search(request):
    posts = Post.objects.all()
    setting = Setting.objects.latest('id')
    qury_object = request.GET.get('key')
    if qury_object:
        posts = Post.objects.filter(Q(title__icontains = qury_object) | Q(description__icontains = qury_object))
    context = {
        'setting' : setting,
        'posts' : posts
    }
    return render(request, 'posts/search.html', context)
    