from django.shortcuts import redirect, get_object_or_404, render, HttpResponse
from .models import Post
from django.core.paginator import Paginator


def index(request):
    return render(request, 'HEXA_Web_Door.html')

def Home(request):
    return render(request, 'Found.html')

def Found(request):
    return render(request, 'Found.html')

def Member(request):
    return render(request, 'Member.html')


def Notice(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 5)

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    return render(request, 'Notice.html', {'posts': posts})

def Notice_write(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.create(title=title, content=content)
        return redirect('Home_app:Notice')
    return render(request, 'Notice_write.html')

def Notice_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'Notice_detail.html', {'post': post})

def Notice_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return redirect('Home_app:Notice_detail', post_id=post.id)

    return render(request, 'Notice_edit.html', {'post': post})

def Notice_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('Home_app:Notice')
    return render(request, 'Notice_delete.html', {'post': post})


def Idea(request):
    return render(request, 'Idea.html')

def Team(request):
    return render(request, 'Team.html')

#suggest
def Suggest(request):
    posts = Post.objects.filter(category='suggestion').order_by('-created_at')  # 건의사항만 필터링
    paginator = Paginator(posts, 5)

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    return render(request, 'Suggest.html', {'posts': posts})

def Suggest_write(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.create(title=title, content=content, category='suggestion')  # 건의사항으로 저장
        return redirect('Home_app:Suggest')
    return render(request, 'Suggest_write.html')


def Suggest_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'Suggest_detail.html', {'post': post})

def Suggest_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return redirect('Home_app:Suggest_detail', post_id=post.id)

    return render(request, 'Suggest_edit.html', {'post': post})

def Suggest_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('Home_app:Suggest')
    return render(request, 'Suggest_delete.html', {'post': post})


#seminar
def Seminar(request):
    posts = Post.objects.filter(category='seminar').order_by('-created_at')  # 건의사항만 필터링
    paginator = Paginator(posts, 5)

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    return render(request, 'Seminar.html', {'posts': posts})

def Seminar_write(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES.get('image')  # 업로드된 이미지 파일
        file = request.FILES.get('file')  # 업로드된 일반 파일
        Post.objects.create(title=title, content=content, category='seminar', image=image, file = file,)  # 건의사항으로 저장
        return redirect('Home_app:Seminar')
    return render(request, 'Seminar_write.html')


def Seminar_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'Seminar_detail.html', {'post': post})

def Seminar_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return redirect('Home_app:Seminar_detail', post_id=post.id)

    return render(request, 'Seminar_edit.html', {'post': post})

def Seminar_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('Home_app:Seminar')
    return render(request, 'Seminar_delete.html', {'post': post})