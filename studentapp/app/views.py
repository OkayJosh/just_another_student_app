from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .forms import (StudentForm, ParentForm, BookForm, LiteracyForm, 
                    AttendanceForm, IncentiveForm, AppraisalForm, 
                    PostingForm, AbsenceRecordForm, OutOfSchoolForm, 
                    ReturnToSchoolForm, FeedingForm)
from .models import Student, Parent

class HomeView(ListView):

class CreateStudentFormView(CreateView):
class UpdateStudentFormView(UpdateView):
class DetailsStudentView(DetailView):

class CreateParentFormView(CreateView):
class UpdateParentFormView(UpdateView):

class CreateBookFormView(CreateView):
class UpdateBookFormView(UpdateView):

class CreateLiteracyFormView(CreateView):
class UpdateLiteracyFormView(UpdateView):

class CreateIncentiveFormView(CreateView):
class UpdateIncentiveFormView(UpdateView):

class CreateAppraisalFormView(CreateView):
class UpdateAppraisalFormView(UpdateView):

class CreateAttendanceFormView(CreateView):
class UpdateAttendanceFormView(UpdateView):

class CreatePostingFormView(CreateView):
class UpdatePostingFormView(UpdateView):

class CreateAbsenceRecordFormView(CreateView):
class UpdateAbsenceRecordFormView(UpdateView):

class CreateOutOfSchoolFormView(CreateView):
class UpdateOutOfSchoolFormView(UpdateView):

class CreateReturnToSchoolFormView(CreateView):
class UpdateReturnToSchoolFormView(UpdateView):

class CreateFeedingFormView(CreateView):
class UpdateFeedingFormView(UpdateView):


