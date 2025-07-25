from django.shortcuts import render
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get(self, request):
        return render(
            request,
            'index.html',
            context={'who': 'Django'}
        )


def about(request):
    tags = ["обучение", "программирование", "python", "oop"]
    return render(
        request,
        "about.html",
        context={"tags": tags},
    )