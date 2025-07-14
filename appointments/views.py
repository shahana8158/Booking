from django.shortcuts import render,redirect
from .models import services,staff,category,doctors,profile,booking

from django.http import HttpResponse
from datetime import time
from datetime import datetime, time

from django.contrib.auth.decorators import login_required
from .forms import bookingForm,profileForm,doctorsForm
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

@login_required(login_url='/login')
def Homefn(request):

    
    return render(request,'Home.html')

@login_required(login_url='/login')
def servicesfn(request):

    x=services.objects.all()
    y=staff.objects.all()

    return render(request,'services.html',{'xyz':x,'abc':y})

@login_required(login_url='/login')
def categoryfn(request):

    
    c=category.objects.all()
    
    return render(request,'category.html',{'cat':c})


@login_required(login_url='/login')
def viewcategoryfn(request,c_id):

    b=doctors.objects.filter(ctry=c_id)

   
    
    return render(request,'viewcategory.html',{'doc':b})


@login_required(login_url='/login')
def doctorsfn(request):

    x=doctors.objects.all()
    
    return render(request,'doctors.html',{'doc':x})





@login_required(login_url='/login')
def bookingfn(request):
     

    if request.method =='POST':
           
            Dname= request.POST['Doctorname']
            pname = request.POST['patientname']
            age = request.POST['Age']
            gen= request.POST['gender']
            num = request.POST['number']
            em= request.POST['email']
            plc= request.POST['place']
            date= request.POST['date']
            time_value= request.POST['time']
            # time_period = request.POST["time_period"] 
            time_v = request.POST["time"]


            try:
                booking_date = datetime.strptime(date, '%Y-%m-%d')  # Convert string to datetime
            except ValueError:
                 messages.add_message(request, messages.ERROR, "Invalid date format.")
                #  return render(request, "booking.html")
                 return redirect('/booking')
                

            if booking_date.weekday() == 6:  # Sunday corresponds to 6
                messages.add_message(request, messages.ERROR, "Appointments cannot be booked on Sundays.")
                return redirect('/booking')
            if booking_date< datetime.today():
                messages.add_message(request, messages.ERROR, "Appointments cannot be booked in the past.")
                # return render(request, "booking.html")
                return redirect('/booking')
                


         
            hour, minute = map(int, time_v.split(":"))

            # if time_period == "PM" and hour != 12:  
            #    hour += 12
            # if time_period == "AM" and hour == 12:  
            #    hour = 0
            
            input_time = time ( hour, minute)
            start_time = time(9, 0)  
            end_time = time(17, 0)

            if not (start_time <= input_time <= end_time):
              messages.add_message(request,messages.ERROR,f" Appointments must be between 9:00 AM to 5:00 PM.")
            #   return render(request, "booking.html")
              return redirect('/booking')
                 
             
            else:
           
             x=booking.objects.create(
                Doctorname=Dname,
                Patientname=pname,
                Age=age,
                Gender=gen,
                Phone=num,
                Email=em,
                Place=plc,
                # Date=date,
                Date=booking_date,
                # AM_PM = time_period ,
                us=request.user,
                # time_period=time_period
                Time=input_time,
                
             )
            x.save()
            messages.add_message(request,messages.SUCCESS,f"Appointment Booked Successfully!") 
            # return render(request,'booking.html')
            return redirect('/booking')
           
    return render(request,'booking.html')
      
                 
    
          

def registerfn(request):
   if request.method =='POST':
      uname = request.POST['username']
      em = request.POST['email']
      fn = request.POST['fname']
      ln = request.POST['lname']
      num = request.POST['pnum']
      pw1= request.POST['password1']
      pw2= request.POST['password2']


      if pw1==pw2: 

        if User.objects.filter(username=uname).exists():
           messages.error(request,"username taken")
       
           return render(request,'register.html')
        
        elif User.objects.filter(email=em).exists():
      
           messages.error(request,"email taken")
           return render(request,'register.html')

           
        else:
         
         User.objects.create_user(username=uname,email=em,first_name=fn,last_name=ln,password=pw1)
         return redirect('/login')

   
      else:
        
           messages.error(request,"password not matching")
           return render(request,'register.html')
   else:
       return render(request,'register.html') 
    


def loginfn(request):
     if request.method =='POST':
         uname = request.POST['username']
         pw1= request.POST['password1']

         x=auth.authenticate(username=uname,password=pw1)
       
         if x:
             auth.login(request,x)

             return redirect('/')
 

         else:
             messages.error(request,"invalid user name or pasword")
             return render(request,'login.html',)
     else:
       return render(request,'login.html',)



def logoutfn(request):
      auth.logout(request)

      return redirect('/login')   


@login_required(login_url='/login')
def profilefn(request):

    if profile.objects.filter(user=request.user.id).exists():

     x=booking.objects.filter(us=request.user.id)
    

     return render(request,'profile.html',{'book':x})
     
    else:
        return redirect('/addprofile')
    
   


def addprofilefn(request):
    if request.method =='POST':
     x=profileForm(request.POST,request.FILES)
     if x.is_valid():
         a=x.save(commit=False)
         a.user=request.user
         a.save()
         return redirect('/profile')

    else:

      f=profileForm()
      return render(request,'addprofile.html',{'form':f})
    

def editprofilefn(request,u_id):

    if request.method =='POST':
       x=profile.objects.get(user=u_id)
       y=profileForm(request.POST,request.FILES,instance=x)
     
       if y.is_valid():
          y.save()
          return redirect('/profile')
       
    else:
        x=profile.objects.get(user=u_id)
        f=profileForm(instance=x)
        return render(request,'editprofile.html',{'form':f})
    



def adddoctorsfn(request):
    if request.method =='POST':
        x=doctorsForm(request.POST,request.FILES)
        if x.is_valid():
            a=x.save(commit=False) 
            a.us=request.user
            a.save()
            return redirect('/doctors')
      
    else:  
        f=doctorsForm()

        return render(request,'adddoctors.html',{'form':f})
    

def editdoctorsfn(request,p_id):
    
    if request.method =='POST':
     
     x=doctors.objects.get(id=p_id)
     y=doctorsForm(request.POST,request.FILES,instance=x)

     if y.is_valid():
        y.save()
        return redirect('/doctors')
       
    else:
        x=doctors.objects.get(id=p_id)
        f=doctorsForm(instance=x)
        return render(request,'editdoctors.html',{'form':f})
    

def deletedoctorsfn(request,p_id):
    x=doctors.objects.get(id=p_id)
    x.delete()
    return redirect('/doctors')
       
 

def editbookingfn(request,p_id):
    
        #    2

     booking_instance = booking.objects.get(id=p_id)

     if request.method == 'POST':
        
        form = bookingForm(request.POST, request.FILES, instance=booking_instance)
       

        if form.is_valid():
            
            form.save()

            return redirect('/profile')
        
            
        # else:
            
        #     return HttpResponse(form.errors)  
            # messages.add_message(request,messages.SUCCESS,f"Appointment Booked Successfully!") 

     else:
        
        form = bookingForm(instance=booking_instance)

    
     return render(request, 'editbooking.html', {'form': form})



    # if request.method =='POST':
     
    #    x=booking.objects.get(id=p_id)
    #    y=bookingForm(request.POST,request.FILES,instance=x)

    #    if y.is_valid():
    #       y.save()
        
    #       return redirect('/profile')
        
    #    else:
    #        return HttpResponse (y.errors)
    
       
    # else:
    #     x=booking.objects.get(id=p_id)
    #     f=bookingForm(instance=x)
    #     return render(request,'editbooking.html',{'form':f})


def cancelbookingfn(request,p_id):
    x=booking.objects.get(id=p_id)
    x.delete()
    return redirect('/profile')