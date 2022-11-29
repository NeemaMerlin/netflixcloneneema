from django.shortcuts import render

# Create your views here.

def main_home(request):
    return render(request,'main_templates/home.html')
def main_about(request):
    return render(request,'main_templates/about.html')
def main_blog(request):
    return render(request,'main_templates/blog.html')
def main_portfolio(request):
    return render(request,'main_templates/portfolio.html')
def main_contact(request):
    return render(request,'main_templates/contact.html')
