from django import forms
from .models import Employee,Emp



class EmployeeForm(forms.ModelForm):

        class Meta:
            model = Employee
            fields = '__all__'
            
            
            
class EmpForm(forms.ModelForm):
    class Meta:
        model=Emp   
        fields = '__all__'        