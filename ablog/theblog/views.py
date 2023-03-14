from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# def home(request):
#     return render(request, 'home.html', {})

def LikeView(request, pk):
     post = get_object_or_404(Post, id=request.POST.get('post_id'))
     post.likes.add(request.user)
     return HttpResponseRedirect(reverse('article-details', args=[str(pk)]))

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    #ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        categories_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["categories_menu"] = categories_menu
        return context

def CategoryView(request, categories):
    category_posts = Post.objects.filter(category=categories.replace("-", " "))
    return render(request, 'categories.html', {'categories':categories.title().replace("-", " "), 'category_posts':category_posts})

def get_context_data(self, *args, **kwargs):
            categories_menu = Category.objects.all()
            context = super(AddPostView, self).get_context_data(*args, **kwargs)
            context["categories_menu"] = categories_menu
            return context    

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        categories_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context["categories_menu"] = categories_menu
        posts_had_likes = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = posts_had_likes.total_likes()
        context["total_likes"] = total_likes
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'
    #fields = ('title', 'body')

    def get_context_data(self, *args, **kwargs):
        categories_menu = Category.objects.all()
        context = super(AddPostView, self).get_context_data(*args, **kwargs)
        context["categories_menu"] = categories_menu
        return context

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

    def get_context_data(self, *args, **kwargs):
        categories_menu = Category.objects.all()
        context = super(AddCategoryView, self).get_context_data(*args, **kwargs)
        context["categories_menu"] = categories_menu
        return context

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
