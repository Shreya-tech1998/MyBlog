from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, ListView, DetailView, TemplateView, DeleteView
from App_Blog.models import Blog, Comment, Likes
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid

# Create your views here.
def blog_list(request):
    return(render(request, 'App_Blog/blog_list.html',context={}))

class blog_list(ListView):
    context_object_name = 'blogs'
    model = Blog
    template_name = 'App_Blog/blog_list.html'

class CreateBlog(LoginRequiredMixin,CreateView):
    model = Blog
    template_name = 'App_Blog/create_blog.html'
    fields = ('blog_title','blog_content','blog_image')
    # from this view class the specified fields from the Blog class will be visible in the create_blog.html page

    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        title = blog_obj.blog_title
        blog_obj.slug = title.replace(" ","-") + "-" + str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('index'))
    
# This view will be called with a dynamic slug_id
def blog_details(request,slug):

    blog = Blog.objects.get(slug=slug)

    return render(request,'App_login/blog_details.html')


    