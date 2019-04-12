from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .forms import (StudentForm, ParentForm, BookForm, LiteracyForm, 
                    AttendanceForm, IncentiveForm, AppraisalForm, 
                    PostingForm, AbsenceRecordForm, OutOfSchoolForm, 
                    ReturnToSchoolForm, FeedingForm)
from .models import (Student, Parent, Book, Literacy, Attendance, Incentive,
                     Appraisal, Posting, AbsenceRecord, OutOfSchool, ReturnToSchool,
                     Feeding)

class HomeView(ListView):
    template_name = 'student/home.html'
    model = Student
    content_type = None 

class CreateStudentFormView(CreateView):
        template_name = 'student/create.html'
        form_class =  StudentForm
        success_url = 'home'
        content_type = None 

        def form_valid(self, form):
                """
                If the form is valid, save the associated model.

                """
                instance = form.save(commit=False)
                instance.created_by = self.request.user
                instance.save()
                self.object = form.save()
                return super().form_valid(form)

class UpdateStudentFormView(UpdateView):
        pk_url_kwarg = 'pk'
        slug_url_kwarg = 'slug' 
        query_pk_and_slug = True
        template_name = 'student/update.html'
        form_class = StudentForm
        success_url = 'home'

class DetailStudentView(DetailView):
        template_name = 'student/details.html'
        model = Student
        content_type = None 
        pk_url_kwarg = 'pk' 
        query_pk_and_slug = True
        slug_url_kwarg = 'slug'

        def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)

                context['parent'] = Parent.objects.get(
                        student = Student.objects.get(id=self.kwargs['pk'])
                        )
                context['book'] = Book.objects.filter(
                        student = Student.objects.get(id=self.kwargs['pk'])
                        )
                context['literacy'] = Literacy.objects.filter(
                        student = Student.objects.get(id=self.kwargs['pk'])
                        )
                context['attendance'] = Attendance.objects.filter(
                        student = Student.objects.get(id=self.kwargs['pk'])
                        )
                context['incentive'] = Incentive.objects.filter(
                        student = Student.objects.get(id=self.kwargs['pk'])
                        )
                context['appraisal'] = Appraisal.objects.filter(
                        student = Student.objects.get(id=self.kwargs['pk'])
                        )
                context['posting'] = Posting.objects.filter(
                        student = Student.objects.get(id=self.kwargs['pk'])
                        )
                context['absence'] = AbsenceRecord.objects.filter(
                        student = Student.objects.get(id=self.kwargs['pk'])
                        )
                context['out'] = OutOfSchool.objects.filter(
                        student = Student.objects.get(id=self.kwargs['pk'])
                        )
                context['return'] = ReturnToSchool.objects.filter(
                        student = Student.objects.get(id=self.kwargs['pk'])
                        )
                context['feeding'] = Feeding.objects.filter(
                        student = Student.objects.get(id=self.kwargs['pk'])
                        )
                return context

class CreateParentFormView(CreateView):
        template_name = 'student/create_parent.html'
        form_class =  ParentForm
        content_type = None
        pk_url_kwarg = 'pk'
        slug_url_kwarg = 'slug'
        success_url = 'home'

        def form_valid(self, form):
                """
                If the form is valid, save the associated model.
                """
                # the pk from the urls is stored in the kwargs
                instance  = form.save(commit=False)
                instance.owned_by = Student.objects.get(id=self.kwargs['pk'])
                instance.save()
                self.object = form.save()
                return super().form_valid(form)

class UpdateParentFormView(UpdateView):
        pk_url_kwarg = 'pk'
        slug_url_kwarg = 'slug' 
        query_pk_and_slug = True
        template_name = 'student/update_parent.html'
        form_class = ParentForm
        success_url = 'home'

class CreateBookFormView(CreateView):
        template_name = 'student/create_book.html'
        form_class =  BookForm
        content_type = None
        pk_url_kwarg = 'pk'
        slug_url_kwarg = 'slug'
        success_url = 'home'

        def form_valid(self, form):
                """
                If the form is valid, save the associated model.
                """
                # the pk from the urls is stored in the kwargs
                instance  = form.save(commit=False)
                instance.owned_by = Student.objects.get(id=self.kwargs['pk'])
                instance.save()
                self.object = form.save()
                return super().form_valid(form)

class UpdateBookFormView(UpdateView):
        pk_url_kwarg = 'pk'
        slug_url_kwarg = 'slug' 
        query_pk_and_slug = True
        template_name = 'student/update_book.html'
        form_class = BookForm
        success_url = 'home'

class CreateLiteracyFormView(CreateView):
        template_name = 'student/create_literacy.html'
        form_class =  LiteracyForm
        content_type = None
        pk_url_kwarg = 'pk'
        slug_url_kwarg = 'slug'
        success_url = 'home'

        def form_valid(self, form):
                """
                If the form is valid, save the associated model.
                """
                # the pk from the urls is stored in the kwargs
                instance  = form.save(commit=False)
                instance.owned_by = Student.objects.get(id=self.kwargs['pk'])
                instance.save()
                self.object = form.save()
                return super().form_valid(form)

class UpdateLiteracyFormView(UpdateView):
        pk_url_kwarg = 'pk'
        slug_url_kwarg = 'slug' 
        query_pk_and_slug = True
        template_name = 'student/update_literacy.html'
        form_class = LiteracyForm
        success_url = 'home'

class CreateIncentiveFormView(CreateView):
        template_name = 'student/create_incentive.html'
        form_class =  BookForm
        content_type = None
        pk_url_kwarg = 'pk'
        slug_url_kwarg = 'slug'
        success_url = 'home'

        def form_valid(self, form):
                """
                If the form is valid, save the associated model.
                """
                # the pk from the urls is stored in the kwargs
                instance  = form.save(commit=False)
                instance.owned_by = Student.objects.get(id=self.kwargs['pk'])
                instance.save()
                self.object = form.save()
                return super().form_valid(form)

class UpdateIncentiveFormView(UpdateView):
        pk_url_kwarg = 'pk'
        slug_url_kwarg = 'slug' 
        query_pk_and_slug = True
        template_name = 'student/update_incentive.html'
        form_class = IncentiveForm
        success_url = 'home'

class CreateAppraisalFormView(CreateView):
        template_name = 'student/create_appraisal.html'
        form_class =  AppraisalForm
        content_type = None
        pk_url_kwarg = 'pk'
        slug_url_kwarg = 'slug'
        success_url = 'home'

        def form_valid(self, form):
                """
                If the form is valid, save the associated model.
                """
                # the pk from the urls is stored in the kwargs
                instance  = form.save(commit=False)
                instance.owned_by = Student.objects.get(id=self.kwargs['pk'])
                instance.save()
                self.object = form.save()
                return super().form_valid(form)

class UpdateAppraisalFormView(UpdateView):
        pk_url_kwarg = 'pk'
        slug_url_kwarg = 'slug' 
        query_pk_and_slug = True
        template_name = 'student/update_appraisal.html'
        form_class = AppraisalForm
        success_url = 'home'

class CreateAttendanceFormView(CreateView):
        template_name = 'student/create_attendance.html'
        form_class =  AttendanceForm
        content_type = None
        pk_url_kwarg = 'pk'
        slug_url_kwarg = 'slug'
        success_url = 'home'

        def form_valid(self, form):
                """
                If the form is valid, save the associated model.
                """
                # the pk from the urls is stored in the kwargs
                instance  = form.save(commit=False)
                instance.owned_by = Student.objects.get(id=self.kwargs['pk'])
                instance.save()
                self.object = form.save()
                return super().form_valid(form)

class UpdateAttendanceFormView(UpdateView):
        pk_url_kwarg = 'pk'
        slug_url_kwarg = 'slug' 
        query_pk_and_slug = True
        template_name = 'student/update_attendance.html'
        form_class = AttendanceForm
        success_url = 'home'

class CreatePostingFormView(CreateView):
        template_name = 'student/create_book.html'
        form_class =  PostingForm
        content_type = None
        pk_url_kwarg = 'pk'
        slug_url_kwarg = 'slug'
        success_url = 'home'

        def form_valid(self, form):
                """
                If the form is valid, save the associated model.
                """
                # the pk from the urls is stored in the kwargs
                instance  = form.save(commit=False)
                instance.owned_by = Student.objects.get(id=self.kwargs['pk'])
                instance.save()
                self.object = form.save()
                return super().form_valid(form)

class UpdatePostingFormView(UpdateView):
        pk_url_kwarg = 'pk'
        slug_url_kwarg = 'slug' 
        query_pk_and_slug = True
        template_name = 'student/update_posting.html'
        form_class = PostingForm
        success_url = 'home'

class CreateAbsenceRecordFormView(CreateView):
        template_name = 'student/create_absence.html'
        form_class =  AbsenceRecordForm
        content_type = None
        pk_url_kwarg = 'pk'
        slug_url_kwarg = 'slug'
        success_url = 'home'

        def form_valid(self, form):
                """
                If the form is valid, save the associated model.
                """
                # the pk from the urls is stored in the kwargs
                instance  = form.save(commit=False)
                instance.owned_by = Student.objects.get(id=self.kwargs['pk'])
                instance.save()
                self.object = form.save()
                return super().form_valid(form)
                
class UpdateAbsenceRecordFormView(UpdateView):
        pk_url_kwarg = 'pk'
        slug_url_kwarg = 'slug' 
        query_pk_and_slug = True
        template_name = 'student/update_absence.html'
        form_class = AbsenceRecordForm
        success_url = 'home'

class CreateOutOfSchoolFormView(CreateView):
        template_name = 'student/create_out.html'
        form_class =  OutOfSchoolForm
        content_type = None
        pk_url_kwarg = 'pk'
        slug_url_kwarg = 'slug'
        success_url = 'home'

        def form_valid(self, form):
                """
                If the form is valid, save the associated model.
                """
                # the pk from the urls is stored in the kwargs
                instance  = form.save(commit=False)
                instance.owned_by = Student.objects.get(id=self.kwargs['pk'])
                instance.save()
                self.object = form.save()
                return super().form_valid(form)

class UpdateOutOfSchoolFormView(UpdateView):
        pk_url_kwarg = 'pk'
        slug_url_kwarg = 'slug' 
        query_pk_and_slug = True
        template_name = 'student/update_out.html'
        form_class = OutOfSchoolForm
        success_url = 'home'

class CreateReturnToSchoolFormView(CreateView):
        template_name = 'student/create_return.html'
        form_class =  ReturnToSchoolForm
        content_type = None
        pk_url_kwarg = 'pk'
        slug_url_kwarg = 'slug'
        success_url = 'home'

        def form_valid(self, form):
                """
                If the form is valid, save the associated model.
                """
                # the pk from the urls is stored in the kwargs
                instance  = form.save(commit=False)
                instance.owned_by = Student.objects.get(id=self.kwargs['pk'])
                instance.save()
                self.object = form.save()
                return super().form_valid(form)

class UpdateReturnToSchoolFormView(UpdateView):
        pk_url_kwarg = 'pk'
        slug_url_kwarg = 'slug' 
        query_pk_and_slug = True
        template_name = 'student/update_return.html'
        form_class = ReturnToSchoolForm
        success_url = 'home'

class CreateFeedingFormView(CreateView):
        template_name = 'student/create_feeding.html'
        form_class =  FeedingForm
        content_type = None
        pk_url_kwarg = 'pk'
        slug_url_kwarg = 'slug'
        success_url = 'home'

        def form_valid(self, form):
                """
                If the form is valid, save the associated model.
                """
                # the pk from the urls is stored in the kwargs
                instance  = form.save(commit=False)
                instance.owned_by = Student.objects.get(id=self.kwargs['pk'])
                instance.save()
                self.object = form.save()
                return super().form_valid(form)

class UpdateFeedingFormView(UpdateView):
        pk_url_kwarg = 'pk'
        slug_url_kwarg = 'slug' 
        query_pk_and_slug = True
        template_name = 'student/update_feeding.html'
        form_class = FeedingForm
        success_url = 'home'


