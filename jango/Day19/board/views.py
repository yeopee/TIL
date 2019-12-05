from django.shortcuts import render,redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET , require_POST

#요청이 get이나 post 설정을 해서 아니면 튕기게 한다. 

@login_required
def new_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        #is_valid는 이것이 유효 하냐 걸러서 save 한다.
        if form.is_valid():
            article = form.save(commit=False) #실제로 저장안함 
            article.author = request.user
            article.save()
            return redirect('board:article_detail',article.id)
    else:
        form = ArticleForm()
    
    context = {'form':form}
    
    return render(request,'board/article_form.html',context)




@require_GET
# Create your views here.
def article_list(request):
    articles = Article.objects.all()
    context = {'articles':articles}
    return render(request,'board/article_list.html', context)


def article_detail(request,article_id):
    article = get_object_or_404(Article, id=article_id)
    comment_form = CommentForm()
    comments = Comment.objects.all()
    context={'article':article,
             'comment_form':comment_form,
             'comments':comments,   
            }
    return render(request,'board/article_detail.html',context)

@login_required
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        print(f'Data 넘어옴')
        if form.is_valid():
            article = form.save()
            return redirect('board:article_detail',article.id)
    else:
        form = ArticleForm(instance=article)
    
    context = {'form':form}
    
    return render(request,'board/article_form.html',context)


@login_required
@require_POST
def new_comment(request, article_id):
    article = get_object_or_404(Article, id = article_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.article_id = article_id
        comment.save() 
    return redirect('board:article_detail',article_id)

@require_POST
def toggle_like(request, article_id):
    article = get_object_or_404(Ariticle, id =article_id)
    user = request.user
    if article.like_users.filter(id=user.id).exists():
    #if user  in article.like_user.all():
        article.like_users.remove(user) 
    else:    
        article.like_users.add(user)
    return redirect('board:article_detail',article.id)
    #request.user.like_articles(article)  위와 같은 말임 