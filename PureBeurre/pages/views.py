from django.shortcuts import render

# Create your views here. à éliminer


def home(request):
    """
    This view renders home template
    """
    return render(request, "pages/home.html")


def legal_notices(request):
    """
    This view renders legal notices template
    """
#-tc- éliminer la ligne vide
    return render(request, "pages/legal_notices.html")


def contact(request):
    """
    This view renders contact template
    """
    return render(request, 'pages/contact.html')
