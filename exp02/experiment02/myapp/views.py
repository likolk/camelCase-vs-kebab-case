from django.shortcuts import render
from django.http import HttpResponse
import csv, uuid
from django.views.decorators.csrf import ensure_csrf_cookie


def index(request):
    return render(request, 'index.html')

def demographics(request):
    return render(request, 'demographics.html')

def questions(request):
    return render(request, 'questions.html')


@ensure_csrf_cookie
def submitDemographics(request):
    print("submitting demographics")
    if request.method == 'POST':
        print("inside POST");
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        education = request.POST.get('education')
        occupation = request.POST.get('occupation')
        comments = request.POST.get('comments')


        with open('demographics.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([age, gender, education, occupation, comments])

        return render(request, 'questions.html', {
            "message": "Submission Successful"})
    
    else:
        return render(request, 'demographics.html')
        






