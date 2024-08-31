from django.shortcuts import render
from .models import app , comments
import random

def index(request):
    featured_apps = app.objects.filter(category='app', sub_category='featured')[:4]
    entertainment_apps = app.objects.filter(category='app', sub_category='entertainment')[:4]
    newly_added_apps = app.objects.filter(category='app', sub_category='newly_added')[:4]
    featured_games = app.objects.filter(category='game', sub_category='featured')[:4]
    adult_games = app.objects.filter(category='game', sub_category='adult')[:4]
    adult_apps = app.objects.filter(category='app', sub_category='adult')[:4]
    socialapps = app.objects.filter(category='app', sub_category='social')[:4]
    communication_apps = app.objects.filter(category='app', sub_category='communication')[:4]

    return render(request, 'allinone/index.html', {'featured_apps':featured_apps, 'entertainment_apps':entertainment_apps, 'newly_added_apps':newly_added_apps, 'featured_games':featured_games, 'adult_games':adult_games, 'adult_apps':adult_apps, 'socialapps':socialapps, 'communication_apps':communication_apps})

# Create your views here.
def game(request):
    featured = app.objects.filter(category='game', sub_category='featured')
    newly_added = app.objects.filter(category='game', sub_category='newly_added')
    adult = app.objects.filter(category='game', sub_category='adult')
    return render(request, 'allinone/game.html', {'featured':featured, 'newly_added':newly_added, 'adult':adult})

def app_view(request):
    featured = app.objects.filter(category='app', sub_category='featured')
    newly_added = app.objects.filter(category='app', sub_category='newly_added')
    adult = app.objects.filter(category='app', sub_category='adult')
    entertainment = app.objects.filter(category='app', sub_category='entertainment')
    social = app.objects.filter(category='app', sub_category='social')
    productive = app.objects.filter(category='app', sub_category='productive')
    communication = app.objects.filter(category='app', sub_category='communication')
    premium = app.objects.filter(category='app', sub_category='premium')
    tools_and_utilities = app.objects.filter(category='app', sub_category='tools_and_utilities')
    editor_choice_apps = app.objects.filter(category='app', sub_category='editor_choice_apps')
    editing_apps = app.objects.filter(category='app', sub_category='editing_apps')
    return render(request, 'allinone/app.html', {'featured':featured, 'newly_added':newly_added, 'adult':adult, 'entertainment':entertainment, 'social':social, 'productive':productive, 'communication':communication, 'premium':premium, 'tools_and_utilities':tools_and_utilities, 'editor_choice_apps':editor_choice_apps, 'editing_apps':editing_apps})


from django.core.paginator import Paginator

def specific_app(request, category, subcat):
    app_data_list = app.objects.filter(category=category, sub_category=subcat)
    paginator = Paginator(app_data_list, 20)
    page_number = request.GET.get('page')
    app_data = paginator.get_page(page_number)
    return render(request, 'allinone/specific_app.html', {'app_data':app_data, 'category': category, 'subcat': subcat})

def app_detail(request, id):
    app_data = app.objects.get(id=id)
    print(app_data)
    return render(request, 'allinone/app_detail.html', {'app':app_data})


def rate(request, id, rate):
    app_data = app.objects.get(id=id)
    app_data.rating = (app_data.rating + rate) / 2
    app_data.rating_no += 1
    app_data.save()
    return render(request, 'allinone/app_detail.html', {'app':app_data , 'msg': 'Rating submitted successfully.'})

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import JsonResponse

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import app  # Ensure this is the correct import
import json

@csrf_exempt
@require_POST
def increase_download(request):
    try:
        # Parse JSON data from request
        data = json.loads(request.body)
        
        # Extract app ID from the data
        app_id = data.get('app_id')
        print('Received app_id:', app_id)

        if not app_id:
            return JsonResponse({'error': 'App ID is required'}, status=400)

        # Get the app and increase its download count
        app_instance = app.objects.get(id=app_id)
        print('App found:', app_instance)
        app_instance.download_no = (app_instance.download_no or 0) + 1
        print('Updated download_no:', app_instance.download_no)
        app_instance.save()
        print('App saved successfully')

        return JsonResponse({'success': True})
    
    except app.DoesNotExist:
        return JsonResponse({'error': 'App not found'}, status=404)
    
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def search(request):
    query = request.GET.get('query')
    print(query,'jjjj')
    app_data_list = app.objects.filter(name__icontains=query)if query else app.objects.none()
    paginator = Paginator(app_data_list, 20)
    page_number = request.GET.get('page')
    app_data = paginator.get_page(page_number)
    return render(request, 'allinone/search.html', {'app_data':app_data, 'query':query})
