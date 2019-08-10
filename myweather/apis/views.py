import requests
from django.shortcuts import render,redirect
from .models import City
from .forms import AddcityForm
from django.contrib import messages


def home(request):
    # url='http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID={9ede6596c8125b4b1f4599a4b40f74ea}'
 



    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=9ede6596c8125b4b1f4599a4b40f74ea'
    if request.method=='POST':
        form=AddcityForm(request.POST)
        if form.is_valid():
            
            new_req=City(city=request.POST['city'])
            new_city=form.cleaned_data.get('city')
            city_count=City.objects.filter(city=new_city).count()
            if city_count==0:
                r=requests.get(url.format(new_city)).json()
                if r['cod']==200:

                    print(r)
                    new_req.save()
                    messages.success(request,f'City has been added sucessfully')
                    return redirect('home')
                else:
                    messages.warning(request, f'This city does not exist!')


            messages.warning(request,f'City has been already taken')

                


    else:
        form=AddcityForm()
    cities=City.objects.order_by('-date')
    
    weather_data=[]
    for city in cities:
        
        

    
        r=requests.get(url.format(city)).json()
        city_weather={
            'city':city,
            'temperature':r['main']['temp'],
            'description':r['weather'][0]['description'],
            'icon':r['weather'][0]['icon']
            

        }
       
        weather_data.append(city_weather)
    
    context={'weather_data':weather_data,'form':form}
    return render(request,'index.html',context)



def delete_city(request,city_name):

    City.objects.get(city=city_name).delete()
    
    return redirect('home')
    
    
