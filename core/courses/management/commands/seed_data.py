# courses/management/commands/seed_data.py
from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
import random

from accounts.models import User, Profile
from courses.models import Category, Course, Lesson, Enrollment, Comment, Rate

fake = Faker()


class Command(BaseCommand):
    help = 'Seed database with fake users, courses, lessons, enrollments, comments, ratings'

    def add_arguments(self, parser):
        parser.add_argument('--users', type=int, default=20, help='Number of users to create')
        parser.add_argument('--courses', type=int, default=10, help='Number of courses to create')

    def handle(self, *args, **options):
        users_count = options['users']
        courses_count = options['courses']

        self.stdout.write('🧹 Cleaning old data...')
        Rate.objects.all().delete()
        Comment.objects.all().delete()
        Enrollment.objects.all().delete()
        Lesson.objects.all().delete()
        Course.objects.all().delete()
        Category.objects.all().delete()
        Profile.objects.exclude(user__is_superuser=True).delete()
        User.objects.exclude(is_superuser=True).delete()

        self.stdout.write('🌱 Seeding started...')

        # --- Admin user ---
        admin, _ = User.objects.get_or_create(
            email='admin@gmail.com',
            defaults={
                'password': 'adminpass',
                'role': 'admin',
                'is_staff': True,
                'is_superuser': True
            }
        )
        Profile.objects.get_or_create(user=admin, first_name=fake.first_name(), last_name=fake.last_name(), bio=fake.paragraph(nb_sentences=5), username='admin')

        # --- Teachers ---
        teachers = []
        for i in range(max(3, users_count // 5)):
            email = f"teacher{i+1}@example.com"
            t, created = User.objects.get_or_create(
                email=email,
                defaults={'password': 'teacherpass', 'role': 'teacher', 'is_staff': True}
            )
            Profile.objects.get_or_create(user=t, first_name=fake.first_name(), last_name=fake.last_name(), bio=fake.paragraph(nb_sentences=5), username=f"teacher{i+1}")
            teachers.append(t)

        # --- Students ---
        students = []
        for i in range(users_count):
            email = f"student{i+1}@example.com"
            u, created = User.objects.get_or_create(
                email=email,
                defaults={'password': 'studentpass', 'role': 'student', 'is_active': True}
            )
            username_base = email.split('@')[0]
            username = username_base
            counter = 1
            while Profile.objects.filter(username=username).exists():
                username = f"{username_base}{counter}"
                counter += 1
            Profile.objects.get_or_create(user=u, first_name=fake.first_name(), last_name=fake.last_name(), bio=fake.paragraph(nb_sentences=5), username=username)
            students.append(u)

        # --- Categories ---
        categories = []
        for name in ['Programming', 'Math', 'Design', 'Business', 'Languages']:
            cat, _ = Category.objects.get_or_create(name=name)
            categories.append(cat)

        # --- Courses & Lessons ---
        courses = []
        for i in range(courses_count):
            teacher = random.choice(teachers)
            course = Course.objects.create(
                teacher=teacher,
                title=fake.sentence(nb_words=4),
                body=fake.paragraph(nb_sentences=5),
                published_at=timezone.now()
            )
            course.category.set(random.sample(categories, k=random.randint(1, 2)))
            courses.append(course)

            # Lessons
            for j in range(random.randint(3, 8)):
                Lesson.objects.create(
                    course=course,
                    title=fake.sentence(nb_words=6),
                    body=fake.paragraph(nb_sentences=10),
                    published_at=timezone.now()
                )

        # --- Enrollments ---
        for student in students:
            chosen_courses = random.sample(courses, k=min(len(courses), random.randint(1, 3)))
            for c in chosen_courses:
                Enrollment.objects.get_or_create(student=student, course=c)

        # --- Comments & Ratings ---
        for c in courses:
            for _ in range(random.randint(1, 6)):
                student = random.choice(students)
                Comment.objects.create(user=student, course=c, comment=fake.sentence(nb_words=12))
                Rate.objects.get_or_create(user=student, course=c, defaults={'score': random.randint(1, 10)})

        self.stdout.write(self.style.SUCCESS('✅ Seeding finished successfully!'))
