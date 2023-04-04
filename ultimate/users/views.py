from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm



# from django.core.mail import send_mail
# from django.conf import settings

# Create your views here.

def register(request):
	# send_mail(
    # subject='A cool subject',
    # message='A stunning message',
    # from_email=settings.EMAIL_HOST_USER,
    # recipient_list=['mglass@posteo.de'])
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! You are now able to log in.')
			return redirect('login')
		else:
			return render(request, 'users/register.html', {'form': form})
	else:
		form = UserRegisterForm()
		return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		#form = UserRegisterForm(request.POST)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated!')
			#redirect here prevents the user from experiencing another POST-request on page reload!
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
		'u_form': u_form,
		'p_form': p_form
	}
	return render(request, 'users/profile.html', context)

# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error
