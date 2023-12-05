from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import csv, uuid
from django.views.decorators.csrf import ensure_csrf_cookie
import json
from django.urls import reverse
from .models import Demographics

def index(request):
    return render(request, 'index.html')

def demographics(request):
    return render(request, 'demographics.html')

def questions(request):
    return render(request, 'questions.html')

@ensure_csrf_cookie
def submitDemographics(request):
    if request.method == 'POST':
        age = request.POST.get('age')
        comments = request.POST.get('comments')
        experience = request.POST.get('experience')
        session_id = str(uuid.uuid4())
        # Create a new entry in the Demographics model
        d = Demographics()
        d.session_id = session_id
        d.age = age
        d.experience = experience
        d.comments = comments
        d.save()
        return redirect(reverse('questions') + f'?session_id={session_id}')
    else:
        return render(request, 'demographics.html')

def save_response(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        session_id = data.get('session_id')
        question = data.get('question')
        answer = data.get('answer')
        time_taken = data.get('time_taken')
        is_correct = data.get('is_correct')

        # retrieve the Demographics entry based on the session_id
        demographics_instance = Demographics.objects.filter(session_id=session_id).first()

        if demographics_instance:
            # append new response data to existing fields plus a spearator
            demographics_instance.questions += question + ','
            demographics_instance.answers += answer + ','
            demographics_instance.time_taken += str(time_taken) + ', '  
            demographics_instance.is_correct += str(is_correct) + ', '
            demographics_instance.save()

            return JsonResponse({'status': 'success'})

        else:
            return JsonResponse({'status': 'failure', 'message': 'Session ID not found'}, status=400)

    return JsonResponse({'status': 'failure', 'message': 'Invalid request method'}, status=400)

import subprocess

def compile_postgresqlToCSV(request):
    try:
        subprocess.run(["python", "postgresqlToCSV.py"])
        return JsonResponse({'message': 'Script executed successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
