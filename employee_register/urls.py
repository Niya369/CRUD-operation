# from django.urls import path,include
# from . import views


# urlpatterns = [

#     path('gh/',views.employee_form ,name='employee_insert'),
#     path('l/',views.employee_list ,name='employee_list'),
#     path('list/',views.employeviews ,name='employee_listujhb'),
#     path('employee/',views.employeeAdd ,name='employee_listjhujhb'),
#     path('',views.EmpView.as_view()),
# ]



# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.employee_form, name='employee_insert'),  # This is now the home page
#     path('list/', views.employee_list, name='employee_list'),
# ]



from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_form, name='employee_insert'),  # default create
    path('list/', views.employee_list, name='employee_list'),
    path('<int:id>/', views.employee_form, name='employee_update'),  # update
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'),  # delete
]

