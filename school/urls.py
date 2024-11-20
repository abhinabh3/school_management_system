from django.urls import path
from .views import StudentViewset,TeacherViewset,ClassViewset,AttendanceViewset,ExaminationViewset,GradeViewset,BookViewset,BorrowRecordViewset,ParentViewset, login, logout, register,get_all_users,CourseViewset


urlpatterns = [

    
    path('users/', get_all_users), 

    path('login/',login),
    path('register/',register),
    path('logout/',logout),

    path("student/", StudentViewset.as_view({
        "get" : "list",
        "post":"create"
    }) ),

    path("student/<int:pk>",StudentViewset.as_view({
        "put" : "update",
        "delete" : "destroy",
        "get" : "retrieve"
    })),
    
    path("teacher/", TeacherViewset.as_view({
        "get" : "list",
        "post":"create"
    }) ),

    path("teacher/<int:pk>",TeacherViewset.as_view({
        "put" : "update",
        "delete" : "destroy",
        "get" : "retrieve"
    })),
    path("class/", ClassViewset.as_view({
        "get" : "list",
        "post":"create"
    }) ),

    path("class/<int:pk>",ClassViewset.as_view({
        "put" : "update",
        "delete" : "destroy",
        "get" : "retrieve"
    })),
    path("course/", CourseViewset.as_view({
        "get" : "list",
        "post":"create"
    }) ),

    path("course/<int:pk>",CourseViewset.as_view({
        "put" : "update",
        "delete" : "destroy",
        "get" : "retrieve"
    })),
    path("attendance/", AttendanceViewset.as_view({
        "get" : "list",
        "post":"create"
    }) ),

    path("attendance/<int:pk>",AttendanceViewset.as_view({
        "put" : "update",
        "delete" : "destroy",
        "get" : "retrieve"
    })),
    path("examination/", ExaminationViewset.as_view({
        "get" : "list",
        "post":"create"
    }) ),

    path("examination/<int:pk>",ExaminationViewset.as_view({
        "put" : "update",
        "delete" : "destroy",
        "get" : "retrieve"
    })),
    path("grade/", GradeViewset.as_view({
        "get" : "list",
        "post":"create"
    }) ),

    path("grade/<int:pk>",GradeViewset.as_view({
        "put" : "update",
        "delete" : "destroy",
        "get" : "retrieve"
    })),
    path("book/", BookViewset.as_view({
        "get" : "list",
        "post":"create"
    }) ),

    path("book/<int:pk>",BookViewset.as_view({
        "put" : "update",
        "delete" : "destroy",
        "get" : "retrieve"
    })),
    path("borrow_record/", BorrowRecordViewset.as_view({
        "get" : "list",
        "post":"create"
    }) ),

    path("borrow_record/<int:pk>",BorrowRecordViewset.as_view({
        "put" : "update",
        "delete" : "destroy",
        "get" : "retrieve"
    })),
    path("parent/", ParentViewset.as_view({
        "get" : "list",
        "post":"create"
    }) ),

    path("parent/<int:pk>",ParentViewset.as_view({
        "put" : "update",
        "delete" : "destroy",
        "get" : "retrieve"
    }))








    
   
]
