from django.shortcuts import render
from django.http import HttpResponse

projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully function ecommerce website.'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'Fully function Portfolio website.'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'Fully function Social Network.'
    },
]


def projects(request):
    page = 'projects'
    number = 46
    context = {'page1': page, 'number': number, 'projects': projectsList}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectobj = None
    for i in projectsList:
        if i['id'] == pk:
            projectobj = i
    return render(request, 'projects/single-project.html', {'project': projectobj})
