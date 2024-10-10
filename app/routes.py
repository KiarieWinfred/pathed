from flask import render_template, redirect, url_for, flash, Blueprint, session
from flask_login import login_user, logout_user, current_user, login_required
from . import db
from .models import User, Doctor
from .forms import PhoneNumberForm, OTPForm, DoctorLoginForm, AppointmentForm
from werkzeug.security import check_password_hash

# Create the blueprint for main routes
main = Blueprint('main', __name__)

# Home route
@main.route('/')
def home():
    return render_template('home.html')

# Patient Login route
@main.route('/patient_login', methods=['GET', 'POST'])
def patient_login():
    phone_form = PhoneNumberForm()
    otp_form = OTPForm()

    # Debugging statements
    print(f"Phone form submitted: {phone_form.validate_on_submit()}")
    print(f"OTP form submitted: {otp_form.validate_on_submit()}")
    print(f"Phone number (submitted): {phone_form.phone_number.data}")
    print(f"OTP code (submitted): {otp_form.otp_code.data}")
    print(f"Session phone number: {session.get('phone_number')}")
    print(f"Session OTP: {session.get('generated_otp')}")

    # Handle phone number submission
    if not session.get('otp_sent') and phone_form.validate_on_submit() and phone_form.phone_number.data:
        phone_number = phone_form.phone_number.data.replace('-', '').replace(' ', '')

        # Simulate sending OTP (hardcoded '123456')
        generated_otp = "123456"
        flash('OTP has been sent to your phone number.', 'info')

        # Store phone number and OTP in session for the next step
        session['phone_number'] = phone_number
        session['generated_otp'] = generated_otp
        session['otp_sent'] = True

        # Debugging: print session info
        print(f"Phone number saved in session: {session['phone_number']}")
        print(f"Generated OTP saved in session: {session['generated_otp']}")

        # Redirect to allow OTP input
        return redirect(url_for('main.patient_login'))

    # Handle OTP submission
    elif session.get('otp_sent') and otp_form.validate_on_submit() and otp_form.otp_code.data:
        otp_code = otp_form.otp_code.data

        # Check if the OTP matches the session-stored value
        if otp_code == session.get('generated_otp'):
            patient = User.query.filter_by(phone_number=session.get('phone_number')).first()

            if patient:
                login_user(patient)
                
                # Clear session data after successful login
                session.pop('generated_otp', None)
                session.pop('phone_number', None)
                session.pop('otp_sent', None)

                # Debugging: successful login
                print("Login successful.")
                return redirect(url_for('main.patient_dashboard'))
            else:
                flash('Phone number not found. Please register first.', 'danger')
        else:
            flash('Invalid OTP. Please try again.', 'danger')

        # Debugging: failed OTP validation
        print("Failed OTP validation.")

    return render_template('patient_login.html', phone_form=phone_form, otp_form=otp_form)


# Appointment booking route
@main.route('/book_appointment', methods=['GET', 'POST'])
@login_required  # Ensure the user is logged in
def book_appointment():
    form = AppointmentForm()
    if form.validate_on_submit():
        # Here you can add logic to book the appointment (e.g., save it to the database)
        flash('Appointment booked successfully!', 'success')
        return redirect(url_for('main.home'))  # Redirect to home or another page after booking
    return render_template('book_appointment.html', form=form)

# Patient Dashboard route
@main.route('/patient_dashboard')
def patient_dashboard():
    if current_user.is_authenticated:
        return render_template('patient_dashboard.html', user=current_user)
    return redirect(url_for('main.patient_login'))

# Doctor Login route
@main.route('/doctor_login', methods=['GET', 'POST'])
def doctor_login():
    form = DoctorLoginForm()
    if form.validate_on_submit():
        email = form.email.data
        doctor = Doctor.query.filter_by(email=email).first()
        if doctor and check_password_hash(doctor.password_hash, form.password.data):
            login_user(doctor)  # Log the doctor in
            return redirect(url_for('main.doctor_dashboard'))  # Redirect to doctor dashboard
        else:
            flash('Invalid email or password.', 'danger')
    return render_template('doctor_login.html', form=form)

# Doctor Dashboard route
@main.route('/doctor_dashboard')
@login_required
def doctor_dashboard():
    if current_user.is_authenticated:
        return render_template('doctor_dashboard.html', user=current_user)
    return redirect(url_for('main.doctor_login'))

# Logout route
@main.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.home'))