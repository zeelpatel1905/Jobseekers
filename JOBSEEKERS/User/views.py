from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect, reverse , get_object_or_404
from django.views.generic.list import ListView
from django.views.generic import DetailView
from itertools import chain
from .models import Profile
from Employer.models import Job_upload
from .forms import ProfileForm
from django.contrib import messages

# Create your views here.
def User_Home_View(request):
    Temp = "User\index.html"
    return render(request, Temp)

@login_required
@transaction.atomic
def Edit_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST or None, request.FILES or None, instance=request.user.profile)
        if profile_form.is_valid():
            print('valid')
            f = profile_form.save(commit=False)
            f.email = request.user.email
            f.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('Employee:Home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'User/profileform.html', {
        'p_form': profile_form
    })

def View_profile(request):
    template = 'User/profile.html'
    return render(request, template, {})


class Job_list(ListView):
    paginate_by = 15
    template_name = 'User/job_list.html'

    def get_queryset(self):
        job = Job_upload.objects.all().order_by("job_upload_date")

        job_list = sorted(
            chain(job),
            key=lambda Job_upload: Job_upload.job_upload_date, reverse=True)
        return job_list

def Job_detail(request, pk):
    template_name = 'User/Job_detail.html'

    job_detail = Job_upload.objects.filter(pk=pk)
    print(job_detail)
    return render(request, template_name, {'job_form':job_detail})

