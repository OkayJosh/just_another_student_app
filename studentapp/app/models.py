from django.db import models

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Student(models.Model):

    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    federal_goverment_code = models.CharField(max_length=300, blank=True, null=True)

    addmission_number_of_student = models.CharField(max_length=300, blank=True, null=True)

    full_name = models.CharField(max_length=300)

    gender = models.CharField(max_length=1, choices=GENDER, blank=True, null=True)

    current_passport_photograph = models.ImageField(default='default.jpg',
                         blank=True, null=True)

    address = models.CharField(max_length=200, default='address', 
                         blank=True, null=True)

    city = models.CharField(max_length=100, default='city', 
                         blank=True, null=True)

    local_government_of_origin = models.CharField(max_length=20,
                         null=True, blank=True, default='local origin')

    state_of_origin = models.CharField(max_length=20, null=True, blank=True, 
                        default='state origin')

    house_number_and_street_name = models.CharField(max_length=300, 
                            blank=True, null=True)

    name_of_town = models.CharField(max_length=300, blank=True, null=True)

    local_government_residence = models.CharField(max_length=20,
                        default='local residence', blank=True, null=True)

    state_residence = models.CharField(max_length=20, null=True, 
                        default='state residence', blank=True)

    date_of_birth = models.DateField( blank=True, null=True)

    place_of_birth = models.CharField(max_length=300, blank=True, null=True)

    finger_print = models.CharField(max_length=300, blank=True, null=True)

    email_address = models.CharField(max_length=300, blank=True, null=True)

    date_of_admision = models.DateField(max_length=300, blank=True, null=True)

    Reason_for_admission = models.CharField(max_length=300, blank=True, null=True)

    admission_entry_point = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.full_name

class Parent(models.Model):

    student = models.OneToOneField(Student, on_delete=models.CASCADE)

    full_name_of_the_father = models.CharField(max_length=300)

    current_passport_photograph_of_the_father = models.ImageField(default='default.jpg', blank=True, null=True)
    
    occupation_of_the_father = models.CharField(max_length=200, default='address', blank=True, null=True)
    contact_address_of_the_father = models.CharField(max_length=200, blank=True, null=True)
    contact_telephone_number_of_the_father = models.CharField(max_length=200, blank=True, null=True)

    full_name_of_the_mother = models.CharField(max_length=300)
    current_passport_photograph_of_the_father = models.ImageField(default='default.jpg', blank=True, null=True)
    occupation_of_the_mother = models.CharField(max_length=200, default='address', blank=True, null=True)
    contact_address_of_the_mother = models.CharField(max_length=200, blank=True, null=True)
    contact_telephone_number_of_the_mother = models.CharField(max_length=200, blank=True, null=True)
    

    def __str__(self):
        return '%s and %s' % (self.full_name_of_the_father, self.full_name_of_the_mother)

class Book(models.Model):
    owned_by = models.ForeignKey(Student, related_name="has_books", on_delete=models.CASCADE)

    title_of_the_text_book = models.CharField(max_length=255)
    date_of_collection = models.DateField(max_length=255, null=True, blank=True)
    distribution_personnel = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return '%s' % (self.title_of_the_text_book)

class Literacy(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    date_of_accessment = models.DateField(blank=True, null=True)
    literacy_level = models.CharField(max_length=100, blank=True, null=True)
    literacy_score = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)], default="3")
    describe_literacy = models.TextField("Describe the Literacy of the Student", null=True, blank=True)
    name_of_assessor = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.literacy_score

class Attendance(models.Model):

    # Many attendance will belong to one student
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    attendance_code = models.CharField(max_length=200, blank=True, null=True)

    date_of_attendance = models.DateField(auto_now_add=True, null=True, blank=True)

    clock_in_time = models.BooleanField(blank=True, null=True)
    clock_out_time = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return '%s is %s' % (self.student, self.present)

class Incentive(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    incentive_code = models.CharField(max_length=50, blank=True, null=True)
    date_of_collection_of_incentive = models.DateField(blank=True, null=True)


    reason_of_incentive = models.CharField(max_length=255, null=True, blank=True)
    name_of_authorizing_personnel = models.CharField(max_length=255, blank=True, null=True)
    cash_paid = models.IntegerField(blank=True, null=True)
    value_of_award_or_gift = models.CharField(max_length=255, blank=True, null=True)
    disbursing_personnel = models.CharField(max_length=255, blank=True, null=True)

class Appraisal(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    
    subject_code = models.CharField(max_length=200, blank=True, null=True)
    date_of_appraisal = models.DateField(blank=True, null=True)

    subject_name = models.CharField(max_length=200, blank=True, null=True)
    subject_examination_score = models.IntegerField(blank=True, null=True)
    persistent_talent_identified = models.CharField(max_length=200, blank=True, null=True)
    name_of_appraiser = models.CharField(max_length=200, blank=True, null=True)
    head_teacher_comment = models.CharField(max_length=200, blank=True, null=True)


    def __str__(self):
        return '%s' % (self.subject_name)
    
class Posting(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    name_of_school = models.CharField(max_length=200, blank=True, null=True)
    date_of_posting = models.DateField("Date of Posting")
    reason_for_posting = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return '%s posted to %s' % (self.student, self.name_of_school)

class AbsenceRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    absence_code = models.CharField(max_length=50)
    date_of_review = models.DateField(blank=True, null=True)

    days_of_absence = models.IntegerField(blank=True, null=True)
    reason_for_absence = models.TextField(blank=True, null=True)
    teachers_comment = models.TextField(blank=True, null=True)

class OutOfSchool(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    out_of_school_code = models.CharField(max_length=200, blank=True, null=True)
    date_of_review = models.DateField(auto_now_add=True, blank=True, null=True)
    summary_of_interview = models.TextField(blank=True, null=True)
    reason_for_dropping_out = models.TextField(blank=True, null=True)
    recommendation = models.TextField(blank=True, null=True)
    recommended_date_of_implementation = models.DateField(blank=True, null=True)
    name_of_interviewer = models.CharField(max_length=200, blank=True, null=True)


class ReturnToSchool(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    return_to_school_code = models.CharField(max_length=200, blank=True, null=True)
    date_of_return = models.DateField(auto_now_add=True, blank=True, null=True)

    out_of_school_duration = models.IntegerField(blank=True, null=True)
    comment_by_recieving_personnel = models.TextField(blank=True, null=True)
    name_of_recieving_personnel = models.CharField(max_length=200, blank=True, null=True)

class Feeding(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    feeding_code = models.CharField(max_length=200, blank=True, null=True)
    date_of_review = models.DateField(auto_now_add=True, blank=True, null=True)

    total_days_of_attendance = models.IntegerField(blank=True, null=True)
    feeding_days = models.IntegerField(blank=True, null=True)
    teachers_comment = models.TextField(blank=True, null=True)
