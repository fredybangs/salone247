from django.http import HttpResponse
from .models import Categories


def index(request):
    all_categories = Categories.objects.all()
    html = ''
    for categories in all_categories:
        url = '/music/' + str(categories.id) + '/'
        html += '<a href="' + url +'">' + str(categories.category_name) + '</a><br>'
    return HttpResponse(html)

def detail(request, categories_id):
    return HttpResponse("<h2>This is Category id: " + str(categories_id) + "</h2>")
