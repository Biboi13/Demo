from django.shortcuts import render

# Create your views here.
def job(request):
    context = {
        
    }
    return render(request, 'jobs/job-job.html', context)