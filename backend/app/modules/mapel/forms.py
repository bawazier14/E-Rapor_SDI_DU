from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class MapelForm(FlaskForm):
    kode = StringField('Kode Mapel', validators=[
        DataRequired(message="Kode tidak boleh kosong"),
        Length(max=20, message="Maksimal 20 karakter")
    ])
    nama = StringField('Nama Mata Pelajaran', validators=[
        DataRequired(message="Nama Mapel tidak boleh kosong"),
        Length(max=100, message="Maksimal 100 karakter")
    ])
    kelompok = SelectField('Kelompok', choices=[
        ('A', 'Kelompok A (Muatan Nasional)'),
        ('B', 'Kelompok B (Muatan Kewilayahan)'),
        ('Mulok', 'Muatan Lokal'),
        ('Ekskul', 'Ekstrakurikuler')
    ], validators=[DataRequired(message="Pilih kelompok mapel")])
    urutan = IntegerField('Urutan Tampil', default=0)
    status_aktif = BooleanField('Status Aktif', default=True)
    submit = SubmitField('Simpan')
