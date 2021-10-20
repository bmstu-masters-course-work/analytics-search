from django.shortcuts import render, redirect

from django.core.paginator import Paginator

from django.views.decorators.csrf import csrf_protect

from .forms import SearchForm


from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

from django.views.decorators.cache import cache_page

from .models import *

def paginate(request, query_set, per_page=2):
    paginator = Paginator(query_set, per_page)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj 

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

def search(tiles, query, cached = False):
    results = []
    for tile in tiles:
        print('cached: ', cached)
        if query in tile['description'] or query in tile['name']:
            if cached:
                tile['source'] = 'Этот ответ был взят из кеша.'
            else:
                tile['source'] ='Этот ответ сохранён в кеш.'
                cache.set('tiles', tiles, timeout=CACHE_TTL)
            results.append(tile)
    return results

def get_tiles(query):
    tiles = []
    if 'tiles' in cache:
        db = cache.get('tiles')
        tiles = search(db, query, cached=True)
    if not tiles:
        db = [tile.to_json() for tile in Tile.objects.all()]
        tiles = search(db, query)
    return tiles


# [MANUAL] GET /search_text/
# render empty search form
# write query + click submit
# [MANUAL] POST /search_text/
# check form and get query from it and redirect
# [REDIRECT] GET /search_text/<query>
# render tiles
@cache_page(CACHE_TTL)
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
            tiles = get_tiles(query)
            page_obj = paginate(request, tiles)
            return render(request, 'search_text.html', {
                'form': form,
                'tiles': tiles, 
                'page_obj': page_obj,
                'string_query': query
            })


def action(request, query='', id=0, action=''):
    # Clickhouse send
    print(query)
    print(id)
    print(action)
    return redirect('search_text', query=query)
