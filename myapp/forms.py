from django import forms
from .models import Professional

class ProfessionalForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Professional
        fields = [
            'first_name',
            'last_name',
            'email',
            'password',
            'confirm_password',
            'location',
            'gender',
            'specialization',
            'experience',
            'education',
            'skills',
            'certification',
            'portfolio_url',
            'profile_picture',
            'licenses',  # Add licenses field
        ]
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'password': 'Password',
            'confirm_password': 'Confirm Password',
            'location': 'Location',
            'gender': 'Gender',
            'specialization': 'Specialization',
            'experience': 'Years of Experience',
            'education': 'Education',
            'skills': 'Skills',
            'certification': 'Certification',
            'portfolio_url': 'Portfolio URL',
            'profile_picture': 'Profile Picture',
            'licenses': 'Licenses',  # Add licenses label
        }
        help_texts = {
            'first_name': 'Enter your first name',
            'last_name': 'Enter your last name',
            'email': 'Enter your email address',
            'password': 'Create a password',
            'confirm_password': 'Confirm your password',
            'location': 'Enter your location',
            'gender': 'Select your gender',
            'specialization': 'Enter your professional specialization',
            'experience': 'Enter your years of experience',
            'education': 'Provide your education details',
            'skills': 'List your skills',
            'certification': 'Add any certifications you have',
            'portfolio_url': 'Add a link to your portfolio (e.g., https://example.com)',
            'profile_picture': 'Upload your profile picture',
            'licenses': 'Add any licenses you hold',  # Add licenses help text
        }
        widgets = {
            'password': forms.PasswordInput(),
            'confirm_password': forms.PasswordInput(),
            'portfolio_url': forms.URLInput(attrs={'placeholder': 'https://example.com'}),
        }

# forms.py
from django import forms
from .models import MentalHealthIssue

class MentalHealthIssueForm(forms.ModelForm):
    class Meta:
        model = MentalHealthIssue
        fields = [
            'age',
            'location',
            'condition',
            'description',
            'diagnosis_date',
            'treatment_plan',
            'support_network',
            'additional_information',
        ]
        labels = {
            'age': 'Age',
            'location': 'Location',
            'condition': 'Condition',
            'description': 'Description',
            'diagnosis_date': 'Diagnosis Date',
            'treatment_plan': 'Treatment Plan',
            'support_network': 'Support Network',
            'additional_information': 'Additional Information',
        }
        help_texts = {
            'age': 'Enter your age',
            'location': 'Enter your location',
            'condition': 'Enter your mental health condition',
            'description': 'Provide a detailed description of your condition',
            'diagnosis_date': 'Date of your diagnosis',
            'treatment_plan': 'Describe your treatment plan',
            'support_network': 'List your support network (friends, family, professionals)',
            'additional_information': 'Any additional information you want to share',
            # Add help text for other fields
        }
