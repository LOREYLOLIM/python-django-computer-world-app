from django.shortcuts import render, get_object_or_404, redirect
from .models import Testimonial, Shopping, Ask, Course
from .forms import TestimonialForm, AskForm, SubscriberForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import random
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def details(request, pk):
    Detail = get_object_or_404(Shopping, pk=pk)
    context = {'Detail':Detail}
    template = 'details.html'
    return render(request, template, context)

def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request, 'invalid credential')
            return redirect('login.html')
    
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username = username).exist():
                messages.info(request, 'Username Taken')
                return redirect('register')

            elif User.objects.filter(email = email).exist():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password = password1, email = email, first_name = first_name, last_name = last_name)
                user.save();
                return redirect('login')

        else:
            messages.info(request,'password not matching......')

        return redirect('index.html')

    else:
        return render(request, 'register.html')


def random_digits():
    return "%0.12d" % random.randint(0, 999999999999)

@csrf_exempt
def new(request):
    if request.method == 'POST':
        sub = Subscriber(email=request.POST['email'], conf_num=random_digits())
        sub.save()
        message = Mail(
            from_email=settings.FROM_EMAIL,
            to_emails=sub.email,
            subject='Newsletter Confirmation',
            html_content='Thank you for signing up for my email newsletter! \
                Please complete the process by \
                <a href="{}/confirm/?email={}&conf_num={}"> clicking here to \
                confirm your registration</a>.'.format(request.build_absolute_uri('/confirm/'),
                                                    sub.email,
                                                    sub.conf_num))
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
        return render(request, 'index.html', {'email': sub.email, 'action': 'added', 'form': SubscriberForm()})
    else:
        return render(request, 'index.html', {'form': SubscriberForm()})

def confirm(request):
    sub = Subscriber.objects.get(email=request.GET['email'])
    if sub.conf_num == request.GET['conf_num']:
        sub.confirmed = True
        sub.save()
        return render(request, 'index.html', {'email': sub.email, 'action': 'confirmed'})
    else:
        return render(request, 'index.html', {'email': sub.email, 'action': 'denied'})

def delete(request):
    sub = Subscriber.objects.get(email=request.GET['email'])
    if sub.conf_num == request.GET['conf_num']:
        sub.delete()
        return render(request, 'index.html', {'email': sub.email, 'action': 'unsubscribed'})
    else:
        return render(request, 'index.html', {'email': sub.email, 'action': 'denied'})

def home(request):
    template = 'index.html'
    shop = Shopping.objects.all()
    context = {'shop':shop}
    return render(request, template, context)

def portfolio(request):
    template = 'portfolio.html'

    return render(request, template)

def contacts(request):
    template = 'contacts.html'

    return render(request, template)

def services(request):
    template = 'services.html'

    return render(request, template)

def testimonial(request):
    if request.method =='POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
        

    else:
        form = TestimonialForm
    template = 'testimonial.html'
    testimonials = Testimonial.objects.filter(Approved_comment=True)
    context = {'testimonials': testimonials, 'form':form}
    return render(request, template, context, form)


def courses(request):
    template = 'courses.html'
    lesson = Course.objects.all()
    context = {'lesson':lesson}
    return render(request, template, context)

def aboutus(request):
    template = 'aboutus.html'

    return render(request, template)

def FAQs(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            form.save() 
    else:
        form = AskForm

    Asking = Ask.objects.filter(Approved = True)
    context = {'Asking':Asking, 'form':form}
    template = 'FAQs.html'
    return render(request, template, context)

def delete(request, id):
    testimonial = get_object_or_404(Testimonial, id=id)
    testimonial.delete()
    return redirect('testimonial')

class Signup(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'



