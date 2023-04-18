# from django.shortcuts import render
# from django.http import HttpResponse
#
# # Create your view here.
#
# def index(request):
#     return HttpResponse("<h2>Главная</h2>")
# def about(request):
#     return HttpResponse("<h2>О сайте</h2>")
# def contact(request):
#     return HttpResponse("<h2>Контакты</h2>")
# def products(request, productid=1):
#     output = "<h2>Продукт № {0}</h2>".format(productid)
#     return HttpResponse(output)
# def users(request, id=1, name='Kseniia'):
#     output = "<h2>Пользователь</h2><h3>id: {0}  Имя: {1} </h3> ".format(id,name)
#     return HttpResponse(output)

# from django.shortcuts import render
# from django.http import HttpResponse
#
# def index(request):
#     return HttpResponse("<h2>Главная</h2>")
#
# def about(request):
#     return HttpResponse("<h2>О сайте</h2>")
#
# def contact(request):
#     return HttpResponse("<h2>Контакты</h2>")
#
# def products(request, productid):
#     category = request.GET.get("cat", "")
#     output = "<h2>Продукт № {0}  Категория: {1}</h2>" .format(productid, category)
#     return HttpResponse(output)
#
# def users(request):
#     id = request.GET.get("id", 1)
#     name = request.GET.get("name", "Максим")
#     output = "<h2>Пользователь</h2><h3>id: {0}  Имя: {1}</h3 >" .format(id, name)
#     return HttpResponse(output)

from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect

def index(request):
    return HttpResponse("Index")
def about(request):
    return HttpResponse("About")
def contact(request):
    return HttpResponseRedirect("/about")
def details(request):
    return HttpResponsePermanentRedirect("/")