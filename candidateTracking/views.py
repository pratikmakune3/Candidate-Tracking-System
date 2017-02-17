from django.http import HttpResponse
from django.template import loader
from candidateTracking.models import Candidate
from django.shortcuts import render

def index(request):
    return render(request, 'candidateTracking/index.html', {})


def candidateName(request):
    form_data = request.POST.dict()
    # import ipdb; ipdb.set_trace()
    name = form_data.get('name')
    dob = form_data.get('dob')
    sex = form_data.get('sex')
    exp = form_data.get('exp')
    resume = form_data.get('resume')
    # import ipdb; ipdb.set_trace()
    Candidate.objects.create(name=name, dob=dob,
                             sex=sex, exp=exp, resume=resume)
    if (name is not None):
        return render(request, 'candidateTracking/success.html', form_data)
    else:
        response_template = loader.get_template('candidateTracking/failure.html')
        return HttpResponse(response_template.render())

def candidateList(request):
    context = Candidate.objects.all()
    # import ipdb; ipdb.set_trace()
    return render(request, 'candidateTracking/candidateList.html', {'context': context})

def candidateDetails(request,id):
    candidate_detail = Candidate.objects.get(id=id).__dict__
    import ipdb; ipdb.set_trace()
    return render(request, 'candidateTracking/candidateDetails.html',  candidate_detail)





