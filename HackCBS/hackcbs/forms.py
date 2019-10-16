from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from hackcbs.models import Patient, Doctor, InsuranceAgent, MedicalHistory

class PatientRegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    age = StringField('Age', validators=[DataRequired(), Length(min=1, max=3)])
    address = TextAreaField('Address', validators=[DataRequired()])
    blood_group = StringField('Blood_group')
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        patient = Patient.query.filter_by(email=email.data).first()
        if patient:
            raise ValidationError('That email is taken. Please choose a different one.')

class DoctorRegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    license_number = StringField('License_number', validators=[DataRequired()])
    clinic_address = TextAreaField('Address', validators=[DataRequired()])
    medical_qualification = TextAreaField('Qualification', validators=[DataRequired()])

class AgentRegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    company_name = StringField('Company', validators=[DataRequired()])
    company_id = StringField('Company_ID', validators=[DataRequired()])
    agent_id = StringField('Agent_ID', validaors=[DataRequired()])
    designation = StringField('Designation')

