from django.shortcuts import render

posts = [
    {
        'author' : 'Vedant Pople',
        'title' : 'Demo post',
        'content' : 'First Post content',
        'date' : 'October 20, 2020'
    },
    {
        'author' : 'Vedant Pople Again',
        'title' : 'Demo post 2',
        'content' : 'First Post content 2',
        'date' : 'October 22, 2020'
    }

]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title' : 'About'})
