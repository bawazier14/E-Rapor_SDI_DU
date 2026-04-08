from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from app.models.user import User

class UserCreateForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=100)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    password_confirm = PasswordField('Konfirmasi Password', validators=[
        DataRequired(), 
        EqualTo('password', message='Password harus sama.')
    ])
    role_id = SelectField('Role', coerce=int, validators=[DataRequired()])
    is_active = BooleanField('Aktif', default=True)
    submit = SubmitField('Simpan Pengguna')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username sudah digunakan. Silakan pilih username lain.')

class UserEditForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=100)])
    role_id = SelectField('Role', coerce=int, validators=[DataRequired()])
    is_active = BooleanField('Aktif')
    submit = SubmitField('Update Pengguna')
    
    def __init__(self, original_username, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username sudah digunakan. Silakan pilih username lain.')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password Baru', validators=[DataRequired(), Length(min=6)])
    password_confirm = PasswordField('Konfirmasi Password Baru', validators=[
        DataRequired(), 
        EqualTo('password', message='Password harus sama.')
    ])
    submit = SubmitField('Reset Password')
