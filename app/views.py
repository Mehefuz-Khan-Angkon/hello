from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'home.html')

def bloghome(request):
    return render(request,'blog-home.html')

def about(request):
    return render(request,'about.html')


def blogpost(request):
    return render(request,'blog-post.html')
def contact(request):
    return render(request,'contact.html')
def faq(request):
    return render(request,'faq.html')
def portfolioitem(request):
    return render(request,'portfolio-item.html')        

def portfoliooverview(request):
    return render(request,'portfolio-overview.html')


def pricing(request):
    return render(request,'pricing.html')


