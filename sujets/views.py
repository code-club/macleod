from sujets.models import Question, Option
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django import forms


class VoteForm(forms.Form):
        vote = forms.IntegerField(widget=forms.HiddenInput)


@login_required
def vote(request):
	if request.method == 'POST':
		option = get_object_or_404(Option, pk=request.POST['vote'])
		if request.user in option.voters.all():
			option.voters.remove(request.user)
		else:
			option.voters.add(request.user)
			option.save()
		return redirect(option.question)
	return redirect('/')