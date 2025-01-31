from django import forms
from django.core.exceptions import ValidationError
# for adding product
from .models import doctors,profile,booking
import datetime



class profileForm(forms.ModelForm):

    class Meta:
        model=profile
        exclude=['user'] 



class bookingForm(forms.ModelForm):

    class Meta:
        model=booking
        exclude=['us'] 
        widgets = {
            'Date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'Time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }


    def clean_Date(self):
        date = self.cleaned_data.get('Date')
        if date:
            if date.weekday() == 6:  # 6 is Sunday
                raise forms.ValidationError("Appointments cannot be booked on Sundays.")
            if date < datetime.date.today():
                raise forms.ValidationError("Appointments cannot be booked in the past.")
        return date

    # Validate Time (e.g., between 9:00 AM and 5:00 PM)
    def clean_Time(self):
        time = self.cleaned_data.get('Time')
        if time:
            start_time = datetime.time(9, 0)  # 9:00 AM
            end_time = datetime.time(17, 0)  # 5:00 PM
            if not (start_time <= time <= end_time):
                raise forms.ValidationError("Time must be between 9:00 AM to 5:00 PM.")
        return time

class doctorsForm(forms.ModelForm):

    class Meta:
        model=doctors
        exclude=['us'] 