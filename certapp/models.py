from django.db import models

class Enrolment(models.Model):
    certificate_code = models.CharField(max_length=100)
    user = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    cohort = models.ForeignKey('Cohort', on_delete=models.DO_NOTHING)
    completion_date = models.DateField(null=True, blank=True,default='1900-01-01')

    class Meta:
        managed = False  # Don't allow Django to manage this table
        db_table = 'students_enrolment'  # Exact table name in the MySQL DB


class Cohort(models.Model):
    course_name = models.CharField(max_length=255)
    certificate_name = models.CharField(max_length=255, default='')
    description = models.TextField()  # Use TextField instead of RichTextField
    image = models.ImageField(upload_to='courses/', blank=True, null=True)
    badge = models.CharField(max_length=20, blank=True)
    start_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_weeks = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    email_content = models.TextField(default='')

    class Meta:
        managed = False  # Prevent Django from creating/modifying this table
        db_table = 'students_cohort'  # Match this with the exact name in MySQL
