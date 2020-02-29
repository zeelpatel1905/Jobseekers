from  django import forms
from .models import Company, Employee, Dept, Designation, Company_service, Job_upload

class DateInput(forms.DateInput):
    input_type = 'Date'
    format = '%m/%d/%Y'
    input_formats = '%m/%d/%Y'

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['company_register_number', 'name', 'company_email', 'company_phone', 'company_fax_number', 'company_category', 'company_services', 'company_total_emp_no', 'company_total_dept', 'company_desc', 'company_logo', 'company_street_name', 'company_city', 'company_states', 'company_pincode', 'company_website']


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['emp_company', 'emp_dept', 'emp_designation', 'name', 'emp_last_name', 'emp_email', 'emp_phone', 'emp_bio', 'emp_birthdate', 'emp_gender', 'emp_id_card', 'emp_experience', 'emp_street_name', 'emp_city', 'emp_states', 'emp_pincode']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter First Name', 'class': 'form-control'}),
            'emp_last_name': forms.TextInput(attrs={'placeholder': 'Enter Last Name', 'class': 'form-control'}),
            'emp_email': forms.EmailInput(attrs={'placeholder': 'Enter Email', 'class': 'form-control'}),
            'emp_phone': forms.NumberInput(attrs={'placeholder': 'Enter Phone Number', 'class': 'form-control'}),
            'emp_bio': forms.TextInput(attrs={'placeholder': 'Enter Bio', 'class': 'form-control'}),
            'emp_experience': forms.NumberInput(attrs={'placeholder': 'Enter Experience', 'class': 'form-control'}),
            'emp_street_name': forms.TextInput(attrs={'placeholder': 'Enter Street Name', 'class': 'form-control'}),
            'emp_pincode': forms.NumberInput(attrs={'placeholder': 'Enter Pincode', 'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['emp_dept'].label = 'Select Dept'
        self.fields['emp_designation'].label = 'Select Designation'
        self.fields['name'].label = ''
        self.fields['emp_last_name'].label = ''
        self.fields['emp_email'].label = ''
        self.fields['emp_phone'].label = ''
        self.fields['emp_bio'].label = ''
        self.fields['emp_birthdate'].label = 'Enter Birth date'
        self.fields['emp_gender'].label = 'Gender'
        self.fields['emp_id_card'].label = 'Select Your Id-Card'
        self.fields['emp_experience'].label = ''
        self.fields['emp_street_name'].label = ''
        self.fields['emp_city'].label = 'Select City'
        self.fields['emp_states'].label = 'Select States'
        self.fields['emp_pincode'].label = ''

class JobuploadForm(forms.ModelForm):
    class Meta:
        model = Job_upload
        fields = ['job_title' , 'job_description' , 'job_salary' , 'job_city' , 'job_states' , 'job_qualification' , 'job_quentity' , 'job_deadline' , 'job_bond_time' , 'job_bond_documents' ]

        widgets = {
            'job_title': forms.TextInput(attrs={'placeholder': 'Job Title', 'class': 'form-control'}),
            'job_description' : forms.Textarea(attrs={'placeholder':'Job Description', 'class':'form-control'}),
            'job_salary' : forms.NumberInput(attrs={'placeholder':'Salary package' , 'class':'form-control'}),
            'job_qualification' : forms.TextInput(attrs={'placeholder' : 'Enter required Qualification', 'class':'form-control'}),
            'job_quentity' : forms.NumberInput(attrs={'placeholder' : 'Enter quentity', 'class':'form-control'}),
            'job_deadline' : DateInput(attrs={'placeholder':'enter deadline', 'class':'form-control'}),
            'job_bond_time' : forms.TextInput(attrs={'placeholder':'Enter bond time', 'class':'form-control'}),
            'job_bond_documents' : forms.Textarea(attrs={'placeholder':'Enter bond conditions', 'class':'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(JobuploadForm, self).__init__(*args, **kwargs)
        self.fields['job_title'].label = ''
        self.fields['job_description'].label = ''
        self.fields['job_salary'].label = ''
        self.fields['job_quentity'].label = ''
        self.fields['job_qualification'].label = ''
        self.fields['job_bond_time'].label = ''
        self.fields['job_bond_documents'].label = ''
        self.fields['job_deadline'].label = 'deadline'


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Dept
        fields = ['dept_name']

class DesignationForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = ['Designation_name']

class CompanyserviceForm(forms.ModelForm):
    class Meta:
        model = Company_service
        fields = ['service_name']

class LoginForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['emp_email', 'emp_password']
        widgets = {
            'emp_email': forms.EmailInput(attrs={'placeholder' : 'Enter Email' ,'class': 'form-control'}),
            'emp_password' : forms.PasswordInput(attrs={'placeholder': 'Enter Password', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['emp_email'].label = ''
        self.fields['emp_password'].label = ''

class forgot_password_form(forms.Form):
    email = forms.CharField(max_length = 50, widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Email'}),)

    def __init__(self, *args, **kwargs):
        super(forgot_password_form, self).__init__(*args, **kwargs)
        self.fields['email'].label = ''


class otp_match_form(forms.Form):
    otp = forms.CharField(max_length = 6, widget= forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your OTP'}))

    def __init__(self, *args, **kwargs):
        super(otp_match_form, self).__init__(*args, **kwargs)
        self.fields['otp'].label = ''


class add_new_password_form(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [ 'emp_password' ]
        widgets = {
            'emp_password': forms.TextInput(attrs={'placeholder': 'Enter Password', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(add_new_password_form, self).__init__(*args, **kwargs)
        self.fields['emp_password'].label = ''
