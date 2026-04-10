from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, TextAreaField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Optional, Email

class GuruForm(FlaskForm):
    nip = StringField('NIP', validators=[Optional(), Length(max=30)])
    nuptk = StringField('NUPTK', validators=[Optional(), Length(max=30)])
    nama_lengkap = StringField('Nama Lengkap', validators=[DataRequired(), Length(max=100)])
    jenis_kelamin = SelectField('Jenis Kelamin', choices=[('L', 'Laki-laki'), ('P', 'Perempuan')], validators=[DataRequired()])
    tempat_lahir = StringField('Tempat Lahir', validators=[Optional(), Length(max=50)])
    tanggal_lahir = DateField('Tanggal Lahir', validators=[Optional()], format='%Y-%m-%d')
    agama = StringField('Agama', validators=[Optional(), Length(max=20)])
    alamat = TextAreaField('Alamat', validators=[Optional()])
    no_hp = StringField('No. HP', validators=[Optional(), Length(max=20)])
    is_active = BooleanField('Status Aktif', default=True)
    
    create_user = BooleanField('Buatkan Akun Login', default=False)
    
    submit = SubmitField('Simpan')
