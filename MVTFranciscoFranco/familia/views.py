
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from familia.models import Familiar



def new_familiar (self,name,last_name, date):

    template = loader.get_template('familia/post_familiar.html')
    
    today =datetime.now()
    dates=date.split("-")
    for i in range(3):
        dates[i]=int(dates[i])
    birth=datetime(dates[0],dates[1],dates[2])
    dif=today-birth
    age=int(dif.days//365.25)

    familiar1 = Familiar(name=name,
                        last_name=last_name,
                        age=age,
                        birth_date=date
                                )
    familiar1.save() # save into the DB

    context_dict = {
            'familiar':  familiar1
    }

    render = template.render(context_dict)
    return HttpResponse(render)




def read_familiar(self,id:int):
    template = loader.get_template('familia/get_familiar.html')

    familiar = Familiar.objects.get(pk=id)
    context_dict = {
        'familiar': familiar
    }
    render = template.render(context_dict)
    return HttpResponse(render)



def all_familiar(self):
    template = loader.get_template('familia/all_familiar.html')
    familiars = Familiar.objects.all()
    context_dict = {
        'familiars': familiars
    }    
    render = template.render(context_dict)
    return HttpResponse(render)    




def probandoTemplate(self):
    name="Francisco"
    last_name="Garcia"
    
    template = loader.get_template("familia/index.html")
    
    context_dict={
        "Familiar":Familiar,
    }
    
    render = template.render(context_dict)
    return HttpResponse(render) 
