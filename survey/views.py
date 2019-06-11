from django.shortcuts import render
from .forms import UserDataForm, QuestionForm
from accounts.models import CustomUser
from .models import Question, Answer
def submit_standart_data(request):
    username = request.user.username
    user = CustomUser.objects.get(username=username)    
    form = UserDataForm(instance=user)
    if request.method == 'GET':
        return render(request, '../templates/analysis.html', {'form': form})
    elif request.method == 'POST':
        if form.is_valid:
            user.age = request.POST['age']
            user.sex = request.POST['sex']
            user.weight = request.POST['weight']
            user.height = request.POST['height']
            user.habbits = request.POST['habbits']
            user.allergia = request.POST['allergia']
            user.save()
            return render(request, '../templates/analysis.html')

def survey(request):
    if request.method == "GET":
        form = QuestionForm()
        question = Question.objects.get(first=True)
        id = question.id
        return render(request, "../templates/survey.html", {'form':form, 'question':question.question, 'id':id, 'info':'This survey asks you several questions about your health and tries to predict your illenss based on answers, take a try!'})
    elif request.method == "POST":  
        form = QuestionForm(request.POST)
        if form.is_valid():
            prev_ques = Question.objects.get(id=request.POST['id'])
            question = prev_ques.curr_question.filter(answer=request.POST['userAns'])[0].next_question
            if(question):
                form = QuestionForm()
                return render(request, "../templates/survey.html", {'form':form , 'question': question.question, 'id': question.id})
            else:
                diagnosis = question = prev_ques.curr_question.filter(answer=request.POST['userAns'])[0].diagnosis
                return render(request, "../templates/survey.html", {'diagnosis' : diagnosis})
            