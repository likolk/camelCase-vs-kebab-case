from django.shortcuts import render
from django.http import HttpResponse
import csv, uuid
from django.views.decorators.csrf import ensure_csrf_cookie
import json
from django.http import JsonResponse

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

        return render(request, 'questions.html', {'session_id': session_id})
    else:
        return render(request, 'demographics.html')



def save_response(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        session_id = data.get('session_id')
        question = data.get('question')
        answer = data.get('answer')
        time_taken = data.get('time_taken')

        # TODO: get the session id, search the csv file, locate the line that corresponds to the session id in the csv file, and add next to it
        # the question, answer, and time_taken
        session_id = str(uuid.uuid4())

        # read existing csv file
        rows = []
        with open('demographics.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                rows.append(row)
        
        # Find the row corresponding to the session ID
        for row in rows:
            if row[0] == session_id:
                row.append(question)
                row.append(answer)
                row.append(time_taken)
                break
        
        # write the updated rows to the csv file
        with open('demographics.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failure'}, status=400)




