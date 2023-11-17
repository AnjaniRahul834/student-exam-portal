from django.shortcuts import render, redirect
from django.http import JsonResponse


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

from .models import Task

from django.contrib.auth.decorators import login_required
from api.forms import SignUpForm, CustomerForm
from django.http import HttpResponseRedirect
# Create your views here.


def home_page_view(request):
    return render(request, 'api/home.html')


@login_required
def exam_page_view(request):
    return render(request, 'api/exams.html')


@login_required
def detail_page_view(request):
    form = CustomerForm()
    if request.method == 'POST':

        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    return render(request, 'api/detail.html', {'form': form})


@login_required
def subject_page_view(request):
    return render(request, 'api/subject.html')


def logout_view(request):
    return render(request, 'api/logout.html')


def signup_view(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request, 'api/signup.html', {'form': form})


@api_view(['GET'])
def apiOverview(request):

    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }

    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):

    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return Response('item deleted')
