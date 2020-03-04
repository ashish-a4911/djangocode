from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader

import requests


# Create your views here.

def index(request):
    
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Hyderabad&appid=d4a0a6bb8ca9328857fcbb44db446a0e')
    res = response.json()

    temp = res['main']['temp']

    desc = res['weather'][0]['description']

    dct = {1: temp, 2: desc}

    return render(request, 'app/index.html', dct)


def detail( request):

    template = loader.get_template('app/detail.html')

    response = { 'foo': 'bar' }

    dct = { 1 : 'temp', 2 : 'desc'}

    return HttpResponse( template.render( response, request))


def solved(request):

    template = loader.get_template('app/solved.html')    

    details = [] 

    while True:
        
        city = 'hyderabad' # input("Enter the city info you want: ")

        if city == 'ashish':
        
            break



        url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=d4a0a6bb8ca9328857fcbb44db446a0e"

        print(url)

        response = requests.get(url)
    
        res = response.json()

        print(city, res['main']['temp'], res['main']['pressure'])

        details.append({'city': city, 'temp':res['main']['temp'], 'pressure': res['main']['pressure'], 'humidity': res['main']['humidity']} )
        
 #       if city == 'ashish':
        break

    response = { 'foo': 'bar' }



    dct = {'key': details }

    print(dct['key'])

    print(details[:])

    return HttpResponse( template.render( response, request))







