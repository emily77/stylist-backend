from django.urls import path
from analysis.views import AnalyzeView
from django.http import JsonResponse

urlpatterns = [
    path('api/analyze/', AnalyzeView.as_view(), name='analyze'),
    path('', lambda request: JsonResponse({'status': 'API Running'})),
]