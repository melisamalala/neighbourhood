from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http  import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import *
from .email import send_welcome_email


@login_required(login_url='/accounts/login/')
def home_projects (request):
    # Display all projects here:

    if request.GET.get('search_term'):
        businesses = Business.search_businesses(request.GET.get('search_term'))

    else:
        businesses = Business.objects.all()


    if request.GET.get('search_term'):
        projects = Project.search_project(request.GET.get('search_term'))

    else:
        projects = Project.objects.all()

    form = NewsLetterForm

    if request.method == 'POST':
        form = NewsLetterForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = NewsLetterRecipients(name=name, email=email)
            recipient.save()
            send_welcome_email(name, email)

            HttpResponseRedirect('home_projects')


    return render(request, 'index.html', {'projects':projects, 'letterForm':form, 'businesses':businesses})



def business(request, id):

    try:
        business = Business.objects.get(pk = id)

    except DoesNotExist:
        raise Http404()

    return render(request, 'business.html', {"business": business})

def project(request, id):

    try:
        project = Project.objects.get(pk = id)

    except DoesNotExist:
        raise Http404()

    current_user = request.user
    comments = Review.get_comment(Review, id)
    latest_review_list=Review.objects.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            design_rating = form.cleaned_data['design_rating']
            content_rating = form.cleaned_data['content_rating']
            usability_rating = form.cleaned_data['usability_rating']
            comment = form.cleaned_data['comment']
            review = Review()
            review.project = project
            review.user = current_user
            review.comment = comment
            review.design_rating = design_rating
            review.content_rating = content_rating
            review.usability_rating = usability_rating
            review.save()

    else:
        form = ReviewForm()

        # return HttpResponseRedirect(reverse('image', args=(image.id,)))

    return render(request, 'image.html', {"project": project,
                                          'form':form,
                                          'comments':comments,
                                          'latest_review_list':latest_review_list})

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('homePage')

    else:
        form = NewImageForm()
    return render(request, 'registration/new_image.html', {"form": form})

@login_required(login_url='/accounts/login/')
def new_business(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewBusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.user = current_user
            business.save()
        return redirect('homePage')

    else:
        form = NewBusinessForm()
    return render(request, 'registration/new_business.html', {"form": form})

@login_required(login_url='/accounts/login/')
def new_business(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewBusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.user = current_user
            business.save()
        return redirect('homePage')

    else:
        form = NewBusinessForm()
    return render(request, 'registration/new_business.html', {"form": form})


@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('homePage')

    else:
        form = NewProjectForm()
    return render(request, 'registration/new_project.html', {"form": form})


@login_required(login_url='/accounts/login/')
def new_neighbourhood(request):
    current_user = request.user
    if request.method == 'POST':
        form = CreateNeighbourhoodForm(request.POST, request.FILES)
        if form.is_valid():
            neighbourhood = form.save(commit=False)
            neighbourhood.user = current_user
            neighbourhood.save()
        return redirect('homePage')

    else:
        form = CreateNeighbourhoodForm()
    return render(request, 'registration/new_neighbourhood.html', {"form": form})





# Viewing a single picture

def user_list(request):
    user_list = User.objects.all()
    context = {'user_list': user_list}
    return render(request, 'user_list.html', context)


@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user = request.user

    if request.method == 'POST':
        form = UpdatebioForm(request.POST, request.FILES, instance=current_user.profile)
        print(form.is_valid())
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('homePage')

    else:
        form = UpdatebioForm()
    return render(request, 'registration/edit_profile.html', {"form": form})

@login_required(login_url='/accounts/login/')
def individual_profile_page(request, username=None):
    if not username:
        username = request.user.username
    # images by user id
    images = Image.objects.filter(user_id=username)

    return render (request, 'registration/user_image_list.html', {'images':images, 'username': username})

def search_projects(request):

    # search for a user by their username
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_projects(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "projects": searched_projects})

    else:
        message = "You haven't searched for any person"
        return render(request, 'search.html', {"message": message})


def search_businesses(request):

    # search for a business by its name
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_businesses = Business.search_businesses(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "businesses": searched_businesses})

    else:
        message = "You haven't searched for any business"
        return render(request, 'search.html', {"message": message})



@login_required(login_url='/accounts/login/')
def individual_profile_page(request, username):
    print(username)
    if not username:
        username = request.user.username
    # images by user id
    images = Image.objects.filter(user_id=username)
    user = request.user
    profile = Profile.objects.get(user=user)
    userf = User.objects.get(pk=username)
    latest_review_list = Review.objects.filter(user_id=username).filter(user_id=username)
    context = {'latest_review_list': latest_review_list}
    if userf:
        print('user found')
        profile = Profile.objects.get(user=userf)
    else:
        print('No suchuser')
    return render (request, 'registration/user_image_list.html', context, {'images':images,
                                                                  'profile':profile,
                                                                  'user':user,
                                                                  'username': username})
def review_list(request):
    latest_review_list = Review.objects.all()
    context = {'latest_review_list':latest_review_list}
    return render(request, 'review_list.html', context)


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'review_detail.html', {'review': review})


def project_list(request):
    project_list = Project.objects.order_by('-title')
    context = {'project_list':project_list}
    return render(request, 'project_list.html', context)


# AJAX functionality

def newsletter(request):
    name = request.POST.get('your_name')
    email= request.POST.get('email')

    recipient= NewsLetterRecipients(name= name, email =email)
    recipient.save()
    send_welcome_email(name, email)
    data= {'success': 'You have been successfully added to the newsletter mailing list'}
    return JsonResponse(data)

@login_required(login_url='/accounts/login/')
def join_neighbourhood(request, id):
    '''
    This view function will implement adding
    '''

    neighbourhood = Neighbourhood.objects.get(pk=id)
    if Join.objects.filter(user_id=request.user).exists():


        Join.objects.filter(user_id=request.user).update(neighbourhood_id=neighbourhood)
    else:

        Join(user_id=request.user, neighbourhood_id=neighbourhood).save()


    return render(request, 'neighbourhoods.html', )