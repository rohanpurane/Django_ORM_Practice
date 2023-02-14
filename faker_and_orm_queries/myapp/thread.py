from threading import Thread
from .models import *
from faker import Faker
fake = Faker()
import random

a = ['Python Developer', 'Django Developer', 'Backend Developer', 'Frontend Developer', 'Fullstack Developer', 'Devops Engineer', 'Algo Expert','Data Scientist','Network Engineer','HR Manager','Project Manager']
class EmployeeThread(Thread):
    def __init__(self, total):
        self.total = total
        Thread.__init__(self)
    
    def run(self):
        try:
            print('Thread Execution Started...!')
            for _ in range(self.total):
                Software_Hub.objects.create(
                    employee_name = fake.name(),
                    employee_address = fake.address(),
                    employee_job_roll = random.choices(a),
                    employee_salary = random.randint(100000, 1500000),
                    employee_age = random.randint(20, 60),
                )
        except Exception as e:
            print('Oops! Something went wrong. Please try again.')