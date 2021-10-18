from django.shortcuts import render, redirect

from django.core.paginator import Paginator

from django.views.decorators.csrf import csrf_protect

# def paginate(request, query_set, per_page=2):
#     paginator = Paginator(query_set, per_page)

#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return page_obj

from .forms import SearchForm

# [MANUAL] GET /search_text/
# render empty search form
# write query + click submit
# [MANUAL] POST /search_text/
# check form and get query from it and redirect
# [REDIRECT] GET /search_text/<query>
# render tiles
def search_text(request, query=''):
    # POST - check and redirect
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            return redirect('search_text', query=form.cleaned_data['search_query'])
        else:
            return redirect('search_text', query='')
    else:
        # GET - send empty form
        if query == '':
            form = SearchForm()
            return render(request, 'search_text.html', {
                'form': form
            })
        # GET - generate tiles and send to client and redis or get from redis and send to client
        else:
            form = SearchForm({'search_query': query})
            return render(request, 'search_text.html', {
                'form': form,
                'tiles': [
                    {
                        'is_active': True,
                        'text': 'text1 FROM ' + query,
                        'query': query,
                        'id': 1,
                    }, {
                        'is_active': True,
                        'text': 'text2 FROM ' + query,
                        'query': query,
                        'id': 2,
                    }, {
                        'is_active': True,
                        'text': 'text3 FROM ' + query,
                        'query': query,
                        'id': 3,
                    },
                ],
            })


def action(request, query='', id=0, action=''):
    # Clickhouse send
    print(query)
    print(id)
    print(action)
    return redirect('search_text', query=query)