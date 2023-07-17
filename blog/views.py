from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

all_news = [
    {
        'id': 1,
        'title': 'Plants can both hear and produce sounds',
        'img_url': 'https://images.indianexpress.com/2023/04/flowers-1200.jpg?w=640',
        'description': 'It’s coming: that great green scream that will shatter our eardrums and change our way of thinking forever! Way back in the 1970s, Peter Tompkins and Christopher Bird published their sensational The Secret Life of Plants (1973), which, among other things, proposed that plants could communicate through sound, only we were unable to hear what they were saying (or screaming). Many of the extraordinary claims made in that book were, however, unsubstantiated, and, to the relief of most of us with sensitive consciences and sentiments, the book withered and died. But it seems that it should still give us pause to think.'
    },
    {
        'id': 1,
        'title': 'Plants can both hear and produce sounds',
        'img_url': 'https://images.indianexpress.com/2023/04/flowers-1200.jpg?w=640',
        'description': 'It’s coming: that great green scream that will shatter our eardrums and change our way of thinking forever! Way back in the 1970s, Peter Tompkins and Christopher Bird published their sensational The Secret Life of Plants (1973), which, among other things, proposed that plants could communicate through sound, only we were unable to hear what they were saying (or screaming). Many of the extraordinary claims made in that book were, however, unsubstantiated, and, to the relief of most of us with sensitive consciences and sentiments, the book withered and died. But it seems that it should still give us pause to think.'
    },
    {
        'id': 1,
        'title': 'Plants can both hear and produce sounds',
        'img_url': 'https://images.indianexpress.com/2023/04/flowers-1200.jpg?w=640',
        'description': 'It’s coming: that great green scream that will shatter our eardrums and change our way of thinking forever! Way back in the 1970s, Peter Tompkins and Christopher Bird published their sensational The Secret Life of Plants (1973), which, among other things, proposed that plants could communicate through sound, only we were unable to hear what they were saying (or screaming). Many of the extraordinary claims made in that book were, however, unsubstantiated, and, to the relief of most of us with sensitive consciences and sentiments, the book withered and died. But it seems that it should still give us pause to think.'
    }
]


def start(request):
    return render(request, 'blog/index.html', {
        'all_news': all_news
    })


def posts(request):
    return HttpResponse('Blog Post')


def posts_detail(request):
    return HttpResponse('Blog Post details')
