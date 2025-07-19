from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get(self, request):
        return redirect(
            reverse(
                'article',
                kwargs={
                    'tags': 'python',
                    'article_id': 42
                }
            )
        )


def about(request):
    tags = ["обучение", "программирование", "python", "oop"]
    return render(
        request,
        "about.html",
        context={"tags": tags},
    )