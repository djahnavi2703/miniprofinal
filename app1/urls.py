from django.urls import path
from . import views
from .views import *
urlpatterns=[

    path('smms/',views.smms,name='smms'),

    path('insert_employee/',views.insert_employee,name='insert_employee'),
    path('view_employee/',views.view_employee,name='view_employee'),
    path('delete_employee/<int:pk>',views.delete_employee,name='delete_employee'),
    path('del_employee/',views.del_employee,name='del_employee'),
    path('update_employee/<int:pk>',views.update_employee,name='update_employee'),
    path('updat_employee/',views.updat_employee,name='updat_employee'),
    path('search_employee/',views.search_employee,name='search_employee'),

    path('edit/<int:id>/', views.batch_edit, name='batch_edit'),
    path('batch/<int:id>/', views.batch_detail, name='batch_detail'),
    path('batch_all_details/',views.batch_all_details,name='batch_all_details'),
    path('BatchId/', views.batch_search, name='BatchId'),
    path('batch_insert/',views.batch_insert,name='batch_insert'),
    path('display_batch/',views.display_batch,name='display_batch'),
    path('process_batch_entry/',views.process_batch_entry,name='process_batch_entry'),
    path('displaybatchinput/',views.displaybatchinput,name='displaybatchinput'),
    path('delete/<pk>',views.delete,name='delete'),
    path('batch_delete/',views.batch_delete,name='batch_delete'),

    path('edit1/<int:id>/', views.course_edit, name='course_edit'),
    path('course/<int:id>/', views.course_detail, name='course_detail'),
    path('course_all_details/',views.course_all_details,name='course_all_details'),
    path('Course/', views.course_search, name='Course'),
    path('course_insert/',views.course_insert,name='course_insert'),
    path('display_course/',views.display_course,name='display_course'),
    path('process_course_entry/',views.process_course_entry,name='process_course_entry'),
    path('displaycourseinput/',views.displaycourseinput,name='displaycourseinput'),
    path('delete1/<pk>',views.delete1,name='delete1'),
    path('course_delete/',views.course_delete,name='course_delete'),

    path('edit2/<int:id>/', views.sem_edit, name='sem_edit'),
    path('sem/<int:id>/', views.sem_detail, name='sem_detail'),
    path('sem_all_details/',views.sem_all_details,name='sem_all_details'),
    path('Sem/', views.sem_search, name='Sem'),
    path('sem_insert/',views.sem_insert,name='sem_insert'),
    path('display_sem/',views.display_sem,name='display_sem'),
    path('process_sem_entry/',views.process_sem_entry,name='process_sem_entry'),
    path('displayseminput/',views.displayseminput,name='displayseminput'),
    path('delete4/<pk>',views.delete4,name='delete4'),
    path('sem_delete/',views.sem_delete,name='sem_delete'),

    path('edit3/<int:id>/', views.exam_edit, name='exam_edit'),
    path('exam/<int:id>/', views.exam_detail, name='exam_detail'),
    path('exam_all_details/',views.exam_all_details,name='exam_all_details'),
    path('ExamId/', views.exam_search, name='ExamId'),
    path('exam_insert/',views.exam_insert,name='exam_insert'),
    path('display_exam/',views.display_exam,name='display_exam'),
    path('process_exam_entry/',views.process_exam_entry,name='process_exam_entry'),
    path('displayexaminput/',views.displayexaminput,name='displayexaminput'),
    path('delete6/<pk>',views.delete6,name='delete6'),
    path('exam_delete/',views.exam_delete,name='exam_delete'),

    path('edit4/<int:id>/', views.paper_edit, name='paper_edit'),
    path('paper/<int:id>/', views.paper_detail, name='paper_detail'),
    path('paper_all_details/',views.paper_all_details,name='paper_all_details'),
    path('PaperCode/', views.paper_search, name='PaperCode'),
    path('paper_insert/',views.paper_insert,name='paper_insert'),
    path('display_paper/',views.display_paper,name='display_paper'),
    path('process_paper_entry/',views.process_paper_entry,name='process_paper_entry'),
    path('displaypaperinput/',views.displaypaperinput,name='displaypaperinput'),
    path('delete5/<pk>',views.delete5,name='delete5'),
    path('paper_delete/',views.paper_delete,name='paper_delete'),

    path('process_student_entry/',views.process_student_entry,name='process_student_entry'),
    path('displaystudentinput/',views.displaystudentinput,name='displaystudentinput'),
    
]

