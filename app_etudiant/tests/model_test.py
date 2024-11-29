from django.test import TestCase
from datetime import date
from app_etudiant.models import *


class CourseModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(name="Mathematics")

    def test_course_creation(self):
        """Test que le modèle Course est correctement créé"""
        self.assertEqual(self.course.name, "Mathematics")
        self.assertEqual(Course.objects.count(), 1)

    def test_course_str_representation(self):
        """Test la représentation en chaîne de caractères du modèle Course"""
        self.assertEqual(str(self.course), "Mathematics")


class StudentModelTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(name="John Doe")

    def test_student_creation(self):
        """Test que le modèle Student est correctement créé"""
        self.assertEqual(self.student.name, "John Doe")
        self.assertEqual(Student.objects.count(), 1)

    def test_student_str_representation(self):
        """Test la représentation en chaîne de caractères du modèle Student"""
        self.assertEqual(str(self.student), "John Doe")


class EnrollmentModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(name="Physics")
        self.student = Student.objects.create(name="Jane Doe")
        self.enrollment = Enrollment.objects.create(
            student=self.student,
            course=self.course,
            enrollment_date=date.today(),
        )

    def test_enrollment_creation(self):
        """Test que le modèle Enrollment est correctement créé"""
        self.assertEqual(Enrollment.objects.count(), 1)
        self.assertEqual(self.enrollment.student, self.student)
        self.assertEqual(self.enrollment.course, self.course)


    def test_enrollment_unique_constraint(self):
        """Test que deux inscriptions identiques ne peuvent pas exister"""
        with self.assertRaises(Exception):  # IntegrityError
            Enrollment.objects.create(
                student=self.student,
                course=self.course,
                enrollment_date=date.today()
            )
