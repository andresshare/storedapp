from django.shortcuts import render


def home_page(request):
    context = {
        "title": "start Project",
        "content": "Welcome to HOME PAGE"
    }
    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        "title": "About Project",
        "content": "Welcome to ABOUT PAGE"
    }
    return render(request, "about_page.html", context)


def contact_page(request):
    context = {
        "title": "contact Project",
        "content": "Welcome to CONTACT PAGE"
    }
    return render(request, "contact/view.html", context)

