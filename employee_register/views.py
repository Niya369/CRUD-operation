"""from django.shortcuts import render
from .forms import  EmployeeForm


# Create your views here.
def employee_list(request):
    return render(request,"employee_register/employee_list.html")

def employee_form(request):
    form = EmployeeForm
    return render(request,"employee_register/employee_form.html",{'forms':form})

def employee_delete(request):
    return """

"""from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

def employee_form(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, "employee_register/employee_form.html", {'form': form})
"""
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .serializers import EmployeeSerializer
# from .models import Employee, Emp
# from rest_framework.views import APIView
# from rest_framework.response import Response

# from rest_framework import status



# from django.shortcuts import render, redirect
# from .forms import EmployeeForm,EmpForm
# from .models import Employee

# def employee_form(request):
    
#     if request.method == 'POST':
#         print("xxxx===",request)
#         form = EmployeeForm(request.POST)
        
#         if form.is_valid():
#             form.save()
#             return redirect('employee_list')
#     else:
#         form = EmployeeForm()
#     return render(request, "employee_register/employee_add.html", {'form': form})

# def employee_list(request):
#     employees = Employee.objects.all()
#     return render(request, "employee_register/employee_list.html", {'employee_list': employees})


# def employeviews(request):
#     k=Emp.objects.all()
#     return render(request, "employee_register/employee_list.html", {'employee_list': k})



# def employeeAdd(request):
#     if request.method == 'POST':
#         form = EmpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('employee_register/employee_list.html')
#     else:
#         form = EmployeeForm()
#     return render(request, "employee_register/employee_add.html", {'form': form})


# class EmpView(APIView):
#     def get(self,request):
#         k=Emp.objects.all()
#         ser=EmployeeSerializer(k,many=True)
#         return Response(ser.data)
#     def post(self,request):
#         ser=EmployeeSerializer(data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data)
#         return Response(ser.errors)
#     def put(self,request):
#         data=request.data
#         pk=data.get("id")
#         employee = Emp.objects.get(id=pk)
#         ser = EmployeeSerializer(employee, data=request.data, partial=True)
#         if ser.is_valid():
#            ser.save()
#            return Response(ser.data)
#         return Response(ser.errors)
#     def delete(self, request):
#         try:
#             data=request.data
#             pk=data.get("id")
#             employee = Emp.objects.get(id=pk)
#             employee.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         except Emp.DoesNotExist:
#             return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)







from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmployeeForm
from .models import Employee



def employee_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = EmployeeForm()
        else:
            employee = get_object_or_404(Employee, pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_add.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = get_object_or_404(Employee, pk=id)
            form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')



def employee_list(request):
    employees = Employee.objects.all()
    return render(request, "employee_register/employee_list.html", {'employee_list': employees})


def employee_delete(request, id):
    employee = get_object_or_404(Employee, pk=id)
    employee.delete()
    return redirect('employee_list')
