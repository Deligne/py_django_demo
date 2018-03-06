from django.http import HttpResponse
from django.shortcuts import render
import markdown
from work.models import article
from django.shortcuts import render, get_object_or_404

def index(request):
    content=article.objects.all().order_by("-pk")
    return render(request,'index.html',{'pages':content})

def page(request,pk):
    post = get_object_or_404(article, pk=pk)
    post.content = markdown.markdown(post.content,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',])
    return render(request, 'page.html', context={'no': post})
