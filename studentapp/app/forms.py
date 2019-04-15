from django.forms import ModelForm
from .models import ( Student, Parent, Book, Literacy, Attendance,
                     Incentive, Appraisal, Posting, AbsenceRecord,
                     OutOfSchool, ReturnToSchool, Feeding)

class StudentForm(ModelForm):
    """
    The student form
    """
    class Meta:
        model = Student
        exclude = ['created_by']

class ParentForm(ModelForm):
    """
    The Parent Form
    """
    class Meta:
        model = Parent
        exclude = ['student']

class BookForm(ModelForm):
    """
    The Book form

    """

    class Meta:
        model = Book
        exclude = ['owned_by']

class  LiteracyForm(ModelForm):
    """
    The Literacy Form

    """
    class Meta:
        model = Literacy
        exclude = ['student']

class  AttendanceForm(ModelForm):
    """
    The Attendance Form
    """
    class Meta:
        model = Attendance
        exclude = ['student']

class IncentiveForm(ModelForm):
    """
    The Incentive Form

    """
    class Meta:
        model = Incentive
        exclude = ['student']

class AppraisalForm(ModelForm):
    """
    The Appraisal Form

    """

    class Meta:
        model = Appraisal
        exclude = ['student']

class PostingForm(ModelForm):
    """
    The Posting Form

    """

    class Meta:
        model = Posting
        exclude = ['student']

class AbsenceRecordForm(ModelForm):
    """
    The Abscence Record Form
OutOfSchool, ReturnToSchool, Feeding
    """

    class Meta:
        model = AbsenceRecord
        exclude = ['student']

class OutOfSchoolForm(ModelForm):
    """
    The OutOfSchool Form

    """
    class Meta:
        model = OutOfSchool
        exclude = ['student']

class ReturnToSchoolForm(ModelForm):
    """
    The Return to school Form

    """

    class Meta:
        model = ReturnToSchool
        exclude = ['student']

class FeedingForm(ModelForm):
    """
    The feeding Form

    """
    class Meta:
        model = Feeding
        exclude = ['student']