from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, Email, Optional

class SekolahForm(FlaskForm):
    nama = StringField('Nama Sekolah', validators=[DataRequired(), Length(max=100)])
    npsn = StringField('NPSN', validators=[DataRequired(), Length(max=20)])
    alamat = TextAreaField('Alamat', validators=[Optional()])
    kode_pos = StringField('Kode Pos', validators=[Optional(), Length(max=10)])
    desa_kelurahan = StringField('Desa/Kelurahan', validators=[Optional(), Length(max=50)])
    kecamatan = StringField('Kecamatan', validators=[Optional(), Length(max=50)])
    kabupaten_kota = StringField('Kabupaten/Kota', validators=[Optional(), Length(max=50)])
    provinsi = StringField('Provinsi', validators=[Optional(), Length(max=50)])
    website = StringField('Website', validators=[Optional(), Length(max=100)])
    email = StringField('Email', validators=[Optional(), Email(), Length(max=100)])
    kepala_sekolah = StringField('Nama Kepala Sekolah', validators=[Optional(), Length(max=100)])
    nip_kepala_sekolah = StringField('NIP Kepala Sekolah', validators=[Optional(), Length(max=30)])
    logo = FileField('Logo Sekolah', validators=[
        Optional(),
        FileAllowed(['jpg', 'jpeg', 'png'], 'Hanya gambar (jpg, jpeg, png) yang diizinkan!')
    ])
    submit = SubmitField('Simpan Perubahan')
