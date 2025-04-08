from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_root(request, format=None):
    base_url = 'https://[REPLACE-THIS-WITH-YOUR-CODESPACE-NAME]-8000.app.github.dev/api/'
    return Response({
        'users': base_url + 'users/?format=api',
        'teams': base_url + 'teams/?format=api',
        'activities': base_url + 'activities/?format=api',
        'leaderboard': base_url + 'leaderboard/?format=api',
        'workouts': base_url + 'workouts/?format=api'
    })

# Create your views here.
