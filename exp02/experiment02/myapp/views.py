from django.shortcuts import render
from django.http import HttpResponse
import csv

def index(request):
    return render(request, 'index.html')

def demographics(request):
    return render(request, 'demographics.html')

def questions(request):
    return render(request, 'questions.html')

def submitDemographics(request):
    if request.method == 'POST':
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        education = request.POST.get('education')
        occupation = request.POST.get('occupation')
        comments = request.POST.get('comments')

        with open('demographics.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([age, gender, education, occupation, comments])
        
        return render(request, 'questions.html')
    else:
        return render(request, 'demographics.html')
        





