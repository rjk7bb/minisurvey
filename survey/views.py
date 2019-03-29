from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import generic
from survey.forms import Question1, Question2, Question3, Question4, Question5, Question7, \
                         Question10, Question11, Question12, Question13, Question14, Question15
from survey.models import User, Player


"Need method that can parse info from game and set user"

'def valid_user(request):'


def quest1(request):

    if request.method == 'POST':
        user = User.objects.get(username='tester')
        form = Question1(request.POST)
        if form.is_valid():
            user.Player.q1 = request.POST.get('number')
            user.save()
            return redirect('survey:q2')
    else:
        form = Question1()
    context = {'form': form}
    return render(request, 'survey/1plus.html', context)


def quest2(request):
    if request.method == 'POST':
        form = Question2(request.POST)
        user = User.objects.get(username='tester')
        if form.is_valid():
            user.Player.q2 = request.POST.get('Options')
            user.save()
            return redirect('survey:q3')
    else:
        form = Question2()
    context = {'form': form}
    return render(request, 'survey/2plus.html', context)


def quest3(request):
    if request.method == 'POST':
        form = Question3(request.POST)
        user = User.objects.get(username='tester')
        if form.is_valid():
            user.Player.q3 = request.POST.get('response')
            user.save()
            return redirect('survey:q4')

    else:
        form = Question3()
    context = {'form': form}
    return render(request, 'survey/3plus.html', context)


def quest4(request):
    if request.method == 'POST':
        form = Question4(request.POST)
        user = User.objects.get(username='tester')
        if form.is_valid():
            user.Player.q4 = request.POST.get('response')
            user.save()
            return redirect('survey:q5')
    else:
        form = Question4()
    context = {'form': form}
    return render(request, 'survey/4plus.html', context)


def quest5(request):
    if request.method == 'POST':
        form = Question5(request.POST)
        user = User.objects.get(username='tester')
        if form.is_valid():
            user.Player.q5 = request.POST.get('Options')
            user.save()
            return redirect('survey:q6')
    else:
        form = Question5()
    context = {'form': form}
    return render(request, 'survey/5plus.html', context)


def quest6(request):
    if request.method == 'POST':
        form = Question5(request.POST)
        user = User.objects.get(username='tester')
        if form.is_valid():
            user.Player.q6 = request.POST.get('Options')
            user.save()
            return redirect('survey:q7')
    else:
        form = Question5()
    context = {'form': form}
    return render(request, 'survey/6plus.html', context)


def quest7(request):
    if request.method == 'POST':
        form = Question7(request.POST)
        user = User.objects.get(username='tester')
        if form.is_valid():
            user.Player.q7a = request.POST.get('yn')
            user.Player.q7b = request.POST.get('response')
            user.Player.q7c = request.POST.get('response2')
            user.save()
            return redirect('survey:q8')
    else:
        form = Question7()
    context = {'form': form}
    return render(request, 'survey/7plus.html', context)


def quest8(request):
    if request.method == 'POST':
        return redirect('survey:q10')
    else:
        form = Question5()
    context = {'form': form}
    return render(request, 'survey/8.html', context)


def quest10(request):
    if request.method == 'POST':
        form = Question10(request.POST)
        user = User.objects.get(username='tester')
        if form.is_valid():
            user.Player.q10a = request.POST.get('option')
            user.Player.q10b = request.POST.get('q2a')
            user.Player.q10c = request.POST.get('q3a')
            user.Player.q10d = request.POST.get('q4a')
            user.save()
            return redirect('survey:q11')
    else:
        form = Question10()
    context = {'form': form}
    return render(request, 'survey/10plus.html', context)


def quest11(request):
    if request.method == 'POST':
        form = Question11(request.POST)
        user = User.objects.get(username='tester')
        if form.is_valid():
            user.Player.q11 = request.POST.get('option')
            user.save()
            return redirect('survey:q12')
    else:
        form = Question11()
    context = {'form': form}
    return render(request, 'survey/11plus.html', context)


def quest12(request):
    if request.method == 'POST':
        form = Question12(request.POST)
        user = User.objects.get(username='tester')
        if form.is_valid():
            user.Player.q12 = request.POST.get('Response')
            user.save()
            return redirect('survey:q13')
    else:
        form = Question12()
    context = {'form': form}
    return render(request, 'survey/12plus.html', context)


def quest13(request):
    if request.method == 'POST':
        form = Question13(request.POST)
        user = User.objects.get(username='tester')
        if form.is_valid():
            user.Player.q13 = request.POST.get('Options')
            user.save()
            return redirect('survey:q14')
    else:
        form = Question13()
    context = {'form': form}
    return render(request, 'survey/13plus.html', context)


def quest14(request):
    if request.method == 'POST':
            form = Question14(request.POST)
            user = User.objects.get(username='tester')
            if form.is_valid():
                user.Player.q14 = request.POST.get('comment')
                user.save()
                return redirect('survey:q15')
    else:
        form = Question14()
    context = {'form': form}
    return render(request, 'survey/14plus.html', context)


def quest15(request):

    if request.method == 'POST':
        form = Question15(request.POST)
        user = User.objects.get(username='tester')
        if form.is_valid():
            user.Player.q15a = request.POST.get('comment1')
            user.Player.q15b = request.POST.get('comment2')
            user.save()
            pass
    else:
        form = Question15()
    context = {'form': form}
    return render(request, 'survey/15plus.html', context)