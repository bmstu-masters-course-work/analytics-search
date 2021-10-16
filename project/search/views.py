from django.shortcuts import render

from django.http import HttpResponse, HttpRequest
from django.core.paginator import Paginator

from django.views.decorators.csrf import csrf_protect

import logging

logger = logging.getLogger(__name__)

# from django.template.defaulttags import register
# from django.urls import reverse

answers = {
    i: {'aid': '1', 'title': 'Answer # {}'.format(i), 'tag': i}
    for i in range(1, 9)
}

# @register.filter
# def get_item(dictionary, key):
#     return dictionary.get(key)

# answers = [{'id': i} for i in range(1,9)]

# tag_names = ["bender", "black-jack", "perl", "python", "Technopark", "MySql", "django", "Mail.ru"]

# questions = {
#     i: {'id': i, 'title': 'Question # {}'.format(i), 'tag': i, 'tag_name': tag_names[i-1], 'answer': answers}
#     for i in range(1, 9)
# }


# tags = {
#     tag_names[i-1]: {'id': i, 'title': 'Tag: {}'.format(tag_names[i-1]), 'question': i}
#     for i in range(1, 9)
# }

# def login(request):
#     return render(request, 'login.html', {})

# def signup(request):
#     return render(request, 'signup.html', {})

def paginate(request, query_set, per_page=2):
    paginator = Paginator(query_set, per_page)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj

@csrf_protect
def answer(request, aid):
    answer = answers.get(aid)
    # answers = question.get('answer')
    # page_obj_a = paginate(request, answers)
    # reverse('polls:index', current_app=self.request.resolver_match.namespace)
    return render(request, 'answer.html', {
        'answer': answer,
        # 'page_obj': page_obj_a
    })

# def tag(request, tid):
#     tags_list = list(tags)
#     tag = tags.get(tid)
#     return render(request, 'tag.html', {
#         'tag': tag,
#         'page_obj': paginate(request, tags_list)
#     })

def search(request):
    # question_list = list(questions.values())
    # page_obj_q = paginate(request, question_list)
    # return render(request, 'analytics-search/project/templates/search.html', {
    return render(request, 'search.html', {
        # 'questions': questions.values(),
        # 'tags': tags.values(),
        # 'page_obj': page_obj_q
    })

@csrf_protect
def search_text(request):
    answers_list = list(answers.values())
    aaa = [4,5,6]
    page_obj_q = paginate(request, answers_list)

    if request.method == 'POST' and 'kek' in request.POST:
        logger.error("hi")
    else:
        logger.error("not hi")

    logger.error("n12345")
        # print("not hi")

    return render(request, 'search_text.html', {
    # return render(request, 'search.html', {
        'text': "text",
        'aaa': aaa,
        'answers': answers.values(),
        # # 'tags': tags.values(),
        'page_obj': page_obj_q,
    })
