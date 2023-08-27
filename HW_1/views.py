from django.shortcuts import render

from django.http import HttpResponse
def text(title, body ):
    return f'<h1>{title}</h1>' \
           f'<p> {body}</p>'

def index (request):
    title='Здравствуйте! Добро пожаловать!'
    body='Это эксперементальный Django сайт.'
    return HttpResponse (text(title,body))
def about (request):
    title = 'Я слушатель курсов в GB,'
    body = 'будущий программист.'
    return HttpResponse (text(title,body))