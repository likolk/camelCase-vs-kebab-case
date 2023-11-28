from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import csv, uuid
from django.views.decorators.csrf import ensure_csrf_cookie
import json
from django.urls import reverse

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
        gender = request.POST.get('gender')
        education = request.POST.get('education')
        occupation = request.POST.get('occupation')
        comments = request.POST.get('comments')

        session_id = str(uuid.uuid4())
        print("session id is:", session_id)

        if not session_id:
            request.session.save()
            session_id = request.session.session_key

        with open('demographics.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([session_id, age, gender, education, occupation, comments])

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
        # age = ''
        # gender = ''
        # education = ''
        # occupation = ''

        # try:
        #     with open('demographics.csv', 'r') as file:
        #         reader = csv.reader(file)
        #         for row in reader:
        #             if row[0] == session_id:
        #                 print("yes it matches")
        #                 age = row[1] 
        #                 gender = row[2]
        #                 education = row[3]
        #                 occupation = row[4]
        #                 break
        # except:
        #     pass


        rows = []
        with open('demographics.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                rows.append(row)
        
        print("ROWS ARRAY CONTENT:", rows)
        found = False
        print("Session ID to find:", session_id)
        for row in rows:
            print("We are at row:", row)
            if row[0] == session_id:
                print("Session ID found in row:", row[0])
                found = True
                row.append(question)
                row.append(answer)
                row.append(time_taken)
                break

        if not found:
            new_row = [question, answer, time_taken]
            rows.append(new_row)

        with open('demographics.csv', 'w') as file:
            writer = csv.writer(file)
            for row in rows:
                writer.writerow(row)

        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'failure'}, status=400)

