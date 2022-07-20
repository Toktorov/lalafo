from django.shortcuts import redirect, render
from apps.settings.models import Setting, AboutUs, Contact, Blog
from apps.posts.models import Post

# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    about = AboutUs.objects.latest('id')
    posts = Post.objects.all().order_by('?')
    blogs = Blog.objects.all()
    context = {
        'setting' : setting,
        'posts' : posts,
        'about' : about,
        'blogs' : blogs,
    }
    return render(request, 'index.html', context)

def contact(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        title = request.POST.get('title')
        phone = request.POST.get('phone')
        problem = request.POST.get('problem')
        contact = Contact.objects.create(name = name, email = email, title = title, phone = phone, problem = problem)
        return redirect('thank_you')
    context = {
        'setting' : setting,
    }
    return render(request, 'contact.html', context)

def thank_you(request):
    setting = Setting.objects.latest('id')
    context = {
        'setting' : setting,
    }
    return render(request, 'users/thank_you.html', context)

#blog-grid-right-sidebar

def blog_detail(request, id):
    setting = Setting.objects.latest('id')
    blog = Blog.objects.get(id = id)
    context = {
        'setting' : setting,
        'blog' : blog,
    }
    return render(request, 'blog-details-right-sidebar.html', context)