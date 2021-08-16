from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Post
import requests

def get_data(request):
    all_blogs = {}
    if 'tag' in request.GET:
        tag = request.GET['tag']
        url = 'https://api.hatchways.io/assessment/blog/posts?tag=%s' % tag
        response = requests.get(url)
        data = response.json()
        blogs = data['posts']

        for i in blogs:
            blog_data = Post(
                author = i['author'],
                authorId = i['authorId'],
                likes = i['likes'],
                popularity = i['popularity'],
                reads = i['reads'],
                tags = i['tags'],
            )
            blog_data.save()
            all_blogs = Post.objects.all().order_by('author')
    return render(request, 'api/blog.html', {"all_blogs": all_blogs})


