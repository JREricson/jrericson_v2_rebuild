from django.shortcuts import redirect, render
from portfolio import views as profile_views


def landing_page(request):
    return redirect("portfolio/")
    # return render(request, "site_main_landing.html", {})
