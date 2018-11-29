from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import generic
from survey.forms import Question1, Question2, Question3, Question4, Question5, Question7, \
                         Question10, Question11, Question12, Question13, Question14, Question15
from survey.models import User, Question, Response


def quest1(request):

    if request.method == 'POST':
        form = Question1(request.POST)
        user = User.objects.get(username='tester')
        q = user.question_set.get(question_text='I did ___% of the work for my group.')
        n = q.response_set.values_list('pk', flat=True)[0]
        a = q.response_set.get(pk=n)
        if form.is_valid():
            a.response_text = request.POST.get('number')
            a.save()
            return redirect('survey:q2')
    else:
        form = Question1()
    context = {'form': form}
    return render(request, 'survey/1plus.html', context)


def quest2(request):
    if request.method == 'POST':
        form = Question2(request.POST)
        user = User.objects.get(username='tester')
        q = user.question_set.get(question_text='Compared to other people in your group, how would you rank your performance on the simulation?')
        n = q.response_set.values_list('pk', flat=True)[0]
        a = q.response_set.get(pk=n)
        if form.is_valid():
            a.response_text = request.POST.get('Options')
            a.save()
            return redirect('survey:q3')
    else:
        form = Question2()
    context = {'form': form}
    return render(request, 'survey/2plus.html', context)


def quest3(request):
    if request.method == 'POST':
        form = Question3(request.POST)
        user = User.objects.get(username='tester')
        q = user.question_set.get(
            question_text='One reason that someone else made a poor decision was:')
        n = q.response_set.values_list('pk', flat=True)[0]
        a = q.response_set.get(pk=n)
        if form.is_valid():
            a.response_text = request.POST.get('response')
            a.save()
            return redirect('survey:q4')

    else:
        form = Question3()
    context = {'form': form}
    return render(request, 'survey/3plus.html', context)


def quest4(request):
    if request.method == 'POST':
        form = Question4(request.POST)
        user = User.objects.get(username='tester')
        q = user.question_set.get(question_text='One reason that you made a poor decision was:')
        n = q.response_set.values_list('pk', flat=True)[0]
        a = q.response_set.get(pk=n)
        if form.is_valid():
            a.response_text = request.POST.get('response')
            a.save()
            return redirect('survey:q5')
    else:
        form = Question4()
    context = {'form': form}
    return render(request, 'survey/4plus.html', context)


def quest5(request):
    if request.method == 'POST':
        form = Question5(request.POST)
        user = User.objects.get(username='tester')
        q = user.question_set.get(question_text='The person in my group with the most power was:')
        n = q.response_set.values_list('pk', flat=True)[0]
        a = q.response_set.get(pk=n)
        if form.is_valid():
            a.response_text = request.POST.get('Options')
            a.save()
            return redirect('survey:q6')
    else:
        form = Question5()
    context = {'form': form}
    return render(request, 'survey/5plus.html', context)


def quest6(request):
    if request.method == 'POST':
        form = Question5(request.POST)
        user = User.objects.get(username='tester')
        q = user.question_set.get(question_text='The person in my group that was most effective was:')
        n = q.response_set.values_list('pk', flat=True)[0]
        a = q.response_set.get(pk=n)
        if form.is_valid():
            a.response_text = request.POST.get('Options')
            a.save()
            return redirect('survey:q7')
    else:
        form = Question5()
    context = {'form': form}
    return render(request, 'survey/6plus.html', context)


def quest7(request):
    if request.method == 'POST':
        form = Question7(request.POST)
        user = User.objects.get(username='tester')

        q = user.question_set.get(question_text='Was there any information that you didn’t share with your group?')
        n = q.response_set.values_list('pk', flat=True)[0]
        a = q.response_set.get(pk=n)

        i = user.question_set.get(question_text='One piece of information I did not share was:')
        o = i.response_set.values_list('pk', flat=True)[0]
        p = i.response_set.get(pk=o)

        t = user.question_set.get(question_text='I chose not to share this information because:')
        y = t.response_set.values_list('pk', flat=True)[0]
        u = t.response_set.get(pk=y)
        if form.is_valid():
            a.response_text = request.POST.get('yn')
            a.save()

            p.response_text = request.POST.get('response')
            p.save()

            u.response_text = request.POST.get('response2')
            u.save()
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

        q = user.question_set.get(question_text='I would invoke/not invoke the 25th Amendment')
        n = q.response_set.values_list('pk', flat=True)[0]
        a = q.response_set.get(pk=n)

        i = user.question_set.get(question_text='One reason for this decision is:')
        o = i.response_set.values_list('pk', flat=True)[0]
        p = i.response_set.get(pk=o)

        t = user.question_set.get(question_text='Another reason is:')
        y = t.response_set.values_list('pk', flat=True)[0]
        u = t.response_set.get(pk=y)

        c = user.question_set.get(question_text='A final reason is:')
        v = c.response_set.values_list('pk', flat=True)[0]
        b = c.response_set.get(pk=v)

        if form.is_valid():
            a.response_text = request.POST.get('option')
            a.save()

            p.response_text = request.POST.get('q2a')
            p.save()

            u.response_text = request.POST.get('q3a')
            u.save()

            b.response_text = request.POST.get('q4a')
            b.save()
            return redirect('survey:q11')
    else:
        form = Question10()
    context = {'form': form}
    return render(request, 'survey/10plus.html', context)


def quest11(request):
    if request.method == 'POST':
        form = Question11(request.POST)
        user = User.objects.get(username='tester')

        q = user.question_set.get(
            question_text='In general, the above questions in this post-simulation questionnaire were clear.')
        n = q.response_set.values_list('pk', flat=True)[0]
        a = q.response_set.get(pk=n)

        if form.is_valid():
            a.response_text = request.POST.get('option')
            a.save()
            return redirect('survey:q12')
    else:
        form = Question11()
    context = {'form': form}
    return render(request, 'survey/11plus.html', context)


def quest12(request):
    if request.method == 'POST':
        form = Question12(request.POST)
        user = User.objects.get(username='tester')

        q = user.question_set.get(
            question_text='Were any of the post-simulation questions unclear? If so, please let us know what items were unclear.')
        n = q.response_set.values_list('pk', flat=True)[0]
        a = q.response_set.get(pk=n)

        if form.is_valid():
            a.response_text = request.POST.get('Response')
            a.save()
            return redirect('survey:q13')
    else:
        form = Question12()
    context = {'form': form}
    return render(request, 'survey/12plus.html', context)


def quest13(request):
    if request.method == 'POST':
        form = Question13(request.POST)
        user = User.objects.get(username='tester')

        q = user.question_set.get(
            question_text='Your impression of this Situation Room Experience as a whole is:')
        n = q.response_set.values_list('pk', flat=True)[0]
        a = q.response_set.get(pk=n)

        if form.is_valid():
            a.response_text = request.POST.get('Options')
            a.save()
            return redirect('survey:q14')
    else:
        form = Question13()
    context = {'form': form}
    return render(request, 'survey/13plus.html', context)


def quest14(request):
    if request.method == 'POST':
            form = Question14(request.POST)
            user = User.objects.get(username='tester')

            q = user.question_set.get(question_text='Are there any changes to this game that you would like to see made? What are they? Any other comments?')
            n = q.response_set.values_list('pk', flat=True)[0]
            a = q.response_set.get(pk=n)

            if form.is_valid():
                a.response_text = request.POST.get('comment')
                a.save()
                return redirect('survey:q15')
    else:
        form = Question14()
    context = {'form': form}
    return render(request, 'survey/14plus.html', context)


def quest15(request):
    if request.method == 'POST':
        form = Question15(request.POST)
        user = User.objects.get(username='tester')

        q = user.question_set.get(question_text='Your Name')
        n = q.response_set.values_list('pk', flat=True)[0]
        a = q.response_set.get(pk=n)

        i = user.question_set.get(question_text='Your Thoughts')
        o = i.response_set.values_list('pk', flat=True)[0]
        p = i.response_set.get(pk=o)

        if form.is_valid():
            a.response_text = request.POST.get('comment1')
            a.save()

            p.response_text = request.POST.get('comment2')
            p.save()
            pass
    else:
        form = Question15()
    context = {'form': form}
    return render(request, 'survey/15plus.html', context)