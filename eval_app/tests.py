from django.test import TestCase

from .models import Employee, Attribute


# Create your tests here.
class EmployeeTestCase(TestCase):
    def test_str_employee_name_is_none(self):
        emp = Employee()
        msg = ''
        self.assertEqual(msg, str(emp))

    def test_str_employee_name_is_not_none(self):
        emp = Employee(name='Saman')
        msg = emp.name
        self.assertEqual(msg, str(emp))

    def test_object_values_are_correct(self):
        employee = Employee.objects.create(name='Hamed', job_title='MD')
        self.assertEqual(employee.job_title, 'MD')


class AttributeTestCase(TestCase):
    def test_str_attributes(self):
        emp = Employee(name='Samann', job_title='dev')
        info = {
            'employee': emp, 'teamwork': 10, 'spirit': 10, 'discipline': 10,
            'creativity': 10
        }
        emp_att = Attribute(**info)

        message = ("%(employee)s >>> Teamwork: %(teamwork)d "
                   "Spirit: %(spirit)d Discipline: %(discipline)d Creativity: "
                   "%(creativity)d") % info
        self.assertEqual(message, str(emp_att))


class SaveTestCase(TestCase):
    def test_save_overall_value_is_correct(self):
        emp = Employee()
        emp.save()
        info = {
            'employee': emp, 'teamwork': 10, 'spirit': 9, 'discipline': 0, 'creativity': 0
        }
        employee_attribute = Attribute(**info)
        employee_attribute.save()
        self.assertEqual(employee_attribute.overall, 19)