from django.urls import path
from .views import (HomeView, CreateStudentFormView, UpdateStudentFormView
                    DetailStudentView, CreateParentFormView, UpdateParentFormView
                    CreateBookFormView, UpdateBookFormView, CreateLiteracyFormView,
                    UpdateLiteracyFormView, CreateIncentiveFormView, 
                    UpdateIncentiveFormView, CreateAppraisalFormView,
                    UpdateAppraisalFormView, CreateAttendanceFormView, 
                    UpdateAttendanceFormView, CreatePostingFormView,
                    UpdatePostingFormView, CreateAbsenceRecordFormView,
                    UpdateAbsenceRecordFormView, CreateOutOfSchoolFormView,
                    UpdateOutOfSchoolFormView, CreateReturnToSchoolFormView,
                    UpdateReturnToSchoolFormView, CreateFeedingFormView,
                    UpdateFeedingFormView)

urlpatterns = [
    path('', HomeView.as_view(), name='home')

    path('/details/<int:pk>/<slug:slug>', DetailStudentView.as_view(), 
    name='details')

    path('/create', CreateStudentFormView.as_view(), name='create')

    path('/update/<int:pk>/<slug:slug>', UpdateStudentFormView.as_view(), 
    name='update')

    path('/parent/<int:pk>/<slug:slug>', CreateParentFormView.as_view(), 
    name='parent')

    path('/parent/update/<int:pk>/<slug:slug>', UpdateParentFormView.as_view(), 
    name='parent_update')

    path('/book/<int:pk>/<slug:slug>', CreateBookFormView.as_view(), 
    name='book')

    path('/book/update/<int:pk>/<slug:slug>', UpdateBookFormView.as_view(), 
    name='book_update')

    path('/literacy/<int:pk>/<slug:slug>', CreateLiteracyFormView.as_view(), 
    name='literacy')

    path('/literacy/update/<int:pk>/<slug:slug>', UpdateLiteracyFormView.as_view(), 
    name='literacy_update')

    path('/incentive/<int:pk>/<slug:slug>', CreateIncentiveFormView.as_view(), 
    name='incentive')

    path('/incentive/update/<int:pk>/<slug:slug>', UpdateIncentiveFormView.as_view(), 
    name='incentive_update')

    path('/appraisal/<int:pk>/<slug:slug>', CreateAppraisalFormViewp.as_view(), 
    name='appraisal')

    path('/appraisal/update/<int:pk>/<slug:slug>', UpdateAppraisalFormView.as_view(), 
    name='appraisal_update')

    path('/attendance/<int:pk>/<slug:slug>', CreateAttendanceFormView.as_view(), 
    name='attendance')

    path('/attendance/update/<int:pk>/<slug:slug>', UpdateAttendanceFormView.as_view(), 
    name='attendance_update')

    path('/posting/<int:pk>/<slug:slug>', CreatePostingFormView.as_view(), 
    name='posting')

    path('/posting/update/<int:pk>/<slug:slug>', UpdatePostingFormView.as_view(), 
    name='posting_update')

    path('/absence/<int:pk>/<slug:slug>', CreateAbsenceRecordFormView.as_view(), 
    name='absence')

    path('/absence/update/<int:pk>/<slug:slug>', UpdateAbsenceRecordFormView.as_view(), 
    name='absence_update')

    path('/out/<int:pk>/<slug:slug>', CreateOutOfSchoolFormView.as_view(), 
    name='out')

    path('/out/update/<int:pk>/<slug:slug>', UpdateOutOfSchoolFormView.as_view(), 
    name='out_update')

    path('/return/<int:pk>/<slug:slug>', CreateReturnToSchoolFormView.as_view(), 
    name='return')

    path('/return/update/<int:pk>/<slug:slug>', UpdateReturnToSchoolFormView.as_view(), 
    name='return_update')
]
