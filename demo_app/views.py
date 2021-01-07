from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Blog, User
from .forms import BlogForm, RegistrationForm


def index(req):
    if not req.user.is_authenticated:
        return render(req, 'index.html', {'page_title': 'Vezbe 13'})
    else:
        return redirect('demo_app:blogs')


@login_required
def blogs(req):
    tmp = Blog.objects.all()
    return render(req, 'blogs.html', {'blogs': tmp})


@login_required
def blog(req, id):
    tmp = get_object_or_404(Blog, id=id)
    return render(req, 'blog.html', {'blog': tmp, 'page_title': tmp.title})


@permission_required('demo_app.change_blog')
def edit(req, id):
    if req.method == 'POST':
        form = BlogForm(req.POST)

        if form.is_valid():
            a = Blog.objects.get(id=id)
            a.title = form.cleaned_data['title']
            a.category = form.cleaned_data['category']
            a.content = form.cleaned_data['content']
            a.save()
            return redirect('demo_app:blogs')
        else:
            return render(req, 'edit.html', {'form': form, 'id': id})
    else:
        a = Blog.objects.get(id=id)
        form = BlogForm(instance=a)
        return render(req, 'edit.html', {'form': form, 'id': id})

@permission_required('blogs.delete_blog')
def delete(request, id):
    temp = Blog.objects.get(pk=id)
    temp.delete()
    return redirect('demo_app:blogs')



@permission_required('demo_app.add_blog')
def new(req):
    if req.method == 'POST':
        form = BlogForm(req.POST)

        if form.is_valid():
            a = Blog(title=form.cleaned_data['title'], category=form.cleaned_data['category'], content=form.cleaned_data['content'], owner=req.user)
            a.save()
            return redirect('demo_app:blogs')
        else:
            return render(req, 'new.html', {'form': form})
    else:
        form = BlogForm()
        return render(req, 'new.html', {'form': form})

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect('demo_app:index')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})
