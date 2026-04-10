from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Optional

class SiswaForm(FlaskForm):
    nisn = StringField('NISN', validators=[Optional(), Length(max=20)])
    nis = StringField('NIS', validators=[Optional(), Length(max=20)])
    nama_lengkap = StringField('Nama Lengkap', validators=[DataRequired(), Length(max=100)])
    jenis_kelamin = SelectField('Jenis Kelamin', choices=[('L', 'Laki-laki'), ('P', 'Perempuan')], validators=[DataRequired()])
    tempat_lahir = StringField('Tempat Lahir', validators=[Optional(), Length(max=50)])
    tanggal_lahir = DateField('Tanggal Lahir', validators=[Optional()], format='%Y-%m-%d')
    agama = StringField('Agama', validators=[Optional(), Length(max=20)])
    alamat = TextAreaField('Alamat', validators=[Optional()])
    
    # Data Orang Tua
    nama_ayah = StringField('Nama Ayah', validators=[Optional(), Length(max=100)])
    nama_ibu = StringField('Nama Ibu', validators=[Optional(), Length(max=100)])
    pekerjaan_ayah = StringField('Pekerjaan Ayah', validators=[Optional(), Length(max=50)])
    pekerjaan_ibu = StringField('Pekerjaan Ibu', validators=[Optional(), Length(max=50)])
    alamat_orang_tua = TextAreaField('Alamat Orang Tua', validators=[Optional()])
    no_hp_orang_tua = StringField('No HP Orang Tua', validators=[Optional(), Length(max=20)])
    
    status_aktif = SelectField('Status', choices=[
        ('aktif', 'Aktif'),
        ('lulus', 'Lulus'),
        ('pindah', 'Pindah'),
        ('keluar', 'Keluar')
    ], default='aktif', validators=[DataRequired()])
    
    submit = SubmitField('Simpan Data Siswa')
