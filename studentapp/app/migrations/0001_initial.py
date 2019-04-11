# Generated by Django 2.1.7 on 2019-04-11 13:03

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AbsenceRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('absence_code', models.CharField(max_length=50)),
                ('date_of_review', models.DateField(blank=True, null=True)),
                ('days_of_absence', models.IntegerField(blank=True, null=True)),
                ('reason_for_absence', models.TextField(blank=True, null=True)),
                ('teachers_comment', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Appraisal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_code', models.CharField(blank=True, max_length=200, null=True)),
                ('date_of_appraisal', models.DateField(blank=True, null=True)),
                ('subject_name', models.CharField(blank=True, max_length=200, null=True)),
                ('subject_examination_score', models.IntegerField(blank=True, null=True)),
                ('persistent_talent_identified', models.CharField(blank=True, max_length=200, null=True)),
                ('name_of_appraiser', models.CharField(blank=True, max_length=200, null=True)),
                ('head_teacher_comment', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance_code', models.CharField(blank=True, max_length=200, null=True)),
                ('date_of_attendance', models.DateField(auto_now_add=True, null=True)),
                ('clock_in_time', models.BooleanField(blank=True, null=True)),
                ('clock_out_time', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_of_the_text_book', models.CharField(max_length=255)),
                ('date_of_collection', models.DateField(blank=True, max_length=255, null=True)),
                ('distribution_personnel', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feeding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feeding_code', models.CharField(blank=True, max_length=200, null=True)),
                ('date_of_review', models.DateField(auto_now_add=True, null=True)),
                ('total_days_of_attendance', models.IntegerField(blank=True, null=True)),
                ('feeding_days', models.IntegerField(blank=True, null=True)),
                ('teachers_comment', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Incentive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incentive_code', models.CharField(blank=True, max_length=50, null=True)),
                ('date_of_collection_of_incentive', models.DateField(blank=True, null=True)),
                ('reason_of_incentive', models.CharField(blank=True, max_length=255, null=True)),
                ('name_of_authorizing_personnel', models.CharField(blank=True, max_length=255, null=True)),
                ('cash_paid', models.IntegerField(blank=True, null=True)),
                ('value_of_award_or_gift', models.CharField(blank=True, max_length=255, null=True)),
                ('disbursing_personnel', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Literacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_accessment', models.DateField(blank=True, null=True)),
                ('literacy_level', models.CharField(blank=True, max_length=100, null=True)),
                ('literacy_score', models.IntegerField(default='3', validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('describe_literacy', models.TextField(blank=True, null=True, verbose_name='Describe the Literacy of the Student')),
                ('name_of_assessor', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OutOfSchool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('out_of_school_code', models.CharField(blank=True, max_length=200, null=True)),
                ('date_of_review', models.DateField(auto_now_add=True, null=True)),
                ('summary_of_interview', models.TextField(blank=True, null=True)),
                ('reason_for_dropping_out', models.TextField(blank=True, null=True)),
                ('recommendation', models.TextField(blank=True, null=True)),
                ('recommended_date_of_implementation', models.DateField(blank=True, null=True)),
                ('name_of_interviewer', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name_of_the_father', models.CharField(max_length=300)),
                ('occupation_of_the_father', models.CharField(blank=True, default='address', max_length=200, null=True)),
                ('contact_address_of_the_father', models.CharField(blank=True, max_length=200, null=True)),
                ('contact_telephone_number_of_the_father', models.CharField(blank=True, max_length=200, null=True)),
                ('full_name_of_the_mother', models.CharField(max_length=300)),
                ('current_passport_photograph_of_the_father', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='')),
                ('occupation_of_the_mother', models.CharField(blank=True, default='address', max_length=200, null=True)),
                ('contact_address_of_the_mother', models.CharField(blank=True, max_length=200, null=True)),
                ('contact_telephone_number_of_the_mother', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_school', models.CharField(blank=True, max_length=200, null=True)),
                ('date_of_posting', models.DateField(verbose_name='Date of Posting')),
                ('reason_for_posting', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReturnToSchool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('return_to_school_code', models.CharField(blank=True, max_length=200, null=True)),
                ('date_of_return', models.DateField(auto_now_add=True, null=True)),
                ('out_of_school_duration', models.IntegerField(blank=True, null=True)),
                ('comment_by_recieving_personnel', models.TextField(blank=True, null=True)),
                ('name_of_recieving_personnel', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('federal_goverment_code', models.CharField(blank=True, max_length=300, null=True)),
                ('addmission_number_of_student', models.CharField(blank=True, max_length=300, null=True)),
                ('full_name', models.CharField(max_length=300)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('current_passport_photograph', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='')),
                ('address', models.CharField(blank=True, default='address', max_length=200, null=True)),
                ('city', models.CharField(blank=True, default='city', max_length=100, null=True)),
                ('local_government_of_origin', models.CharField(blank=True, default='local origin', max_length=20, null=True)),
                ('state_of_origin', models.CharField(blank=True, default='state origin', max_length=20, null=True)),
                ('house_number_and_street_name', models.CharField(blank=True, max_length=300, null=True)),
                ('name_of_town', models.CharField(blank=True, max_length=300, null=True)),
                ('local_government_residence', models.CharField(blank=True, default='local residence', max_length=20, null=True)),
                ('state_residence', models.CharField(blank=True, default='state residence', max_length=20, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('place_of_birth', models.CharField(max_length=300)),
                ('finger_print', models.CharField(blank=True, max_length=300, null=True)),
                ('email_address', models.CharField(blank=True, max_length=300, null=True)),
                ('date_of_admision', models.DateField(blank=True, max_length=300, null=True)),
                ('Reason_for_admission', models.CharField(blank=True, max_length=300, null=True)),
                ('admission_entry_point', models.CharField(blank=True, max_length=300, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='returntoschool',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Student'),
        ),
        migrations.AddField(
            model_name='posting',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Student'),
        ),
        migrations.AddField(
            model_name='parent',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Student'),
        ),
        migrations.AddField(
            model_name='outofschool',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Student'),
        ),
        migrations.AddField(
            model_name='literacy',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Student'),
        ),
        migrations.AddField(
            model_name='incentive',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Student'),
        ),
        migrations.AddField(
            model_name='feeding',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Student'),
        ),
        migrations.AddField(
            model_name='book',
            name='owned_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='has_books', to='app.Student'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Student'),
        ),
        migrations.AddField(
            model_name='appraisal',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Student'),
        ),
        migrations.AddField(
            model_name='absencerecord',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Student'),
        ),
    ]
