
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.home, name="home"),
    path('about/',views.about, name="about"),
    path('',views.bloghome, name="bloghome"),
    path('',views.blogpost, name="blogpost"),
    path('',views.contact, name="contact"),
    path('',views.faq, name="faq"),
    path('',views.portfolioitem, name="portfolioitem"),
    path('',views.portfoliooverview, name="portfoliooverview"),
    path('',views.pricing, name="pricing"),

]
