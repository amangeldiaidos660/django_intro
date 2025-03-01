from django.shortcuts import get_object_or_404, redirect, render
from .forms import BlogForm
from .models import Blog

def blog_list_and_add(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs')
    else:
        form = BlogForm()

    blogs = Blog.objects.all()
    return render(request, 'blog_list.html', {'form': form, 'blogs': blogs})

def delete_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    blog.delete()
    return redirect('blogs')
