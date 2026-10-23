from django.shortcuts import redirect


def landing_page(request):
    return redirect("portfolio/")
    # return render(request, "site_main_landing.html", {})
