from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def register(request):
    form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})


def confirm_register(request):
    dados = {}

    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        user.is_staff = True
        user.save()
        dados['message'] =\
            u'Welcome {nome}'.format(nome=user.username)
        
        return render(request, 'index.html', dados)
    
    else:
        dados = {}
        dados['form'] = form
        
        return render(request, 'registration/register.html', {'form': form})


def dashboard(request):
    return render(request, 'dashboard.html')


def password_confirmation(request, template_name='registration/reset_succefull.html'):
    return render(request, template_name, {})


def reset_confirm(request, uidb64=None, token=None):
    return password_reset_confirm(request, template_name='registration/password_reset_confirm.html',
        uidb64=uidb64, token=token, post_reset_redirect=reverse('url_reset_suceful'))


def reset(request):
    return password_reset(request, template_name='registration/password_reset_form.html',
        email_template_name='registration/password_reset_email.html',
        subject_template_name='registration/password_reset_subject.txt',
        post_reset_redirect=reverse('url_login'))