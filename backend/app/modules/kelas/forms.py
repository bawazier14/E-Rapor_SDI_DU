from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange, ValidationError
from app.models.kelas import Kelas

class KelasForm(FlaskForm):
    tingkat = IntegerField('Tingkat (Angka)', validators=[
        DataRequired(message="Tingkat harus diisi"),
        NumberRange(min=1, max=12, message="Tingkat harus antara 1-12")
    ])
    nama_tingkat = StringField('Nama Tingkat (e.g. Kelas 1)', validators=[DataRequired(message="Nama tingkat harus diisi")])
    fase = SelectField('Fase (Kurikulum Merdeka)', choices=[
        ('', '-- Pilih Fase --'),
        ('A', 'Fase A (Kelas 1-2)'),
        ('B', 'Fase B (Kelas 3-4)'),
        ('C', 'Fase C (Kelas 5-6)'),
        ('D', 'Fase D (Kelas 7-9)'),
        ('E', 'Fase E (Kelas 10)'),
        ('F', 'Fase F (Kelas 11-12)')
    ], validators=[DataRequired(message="Fase harus dipilih")])
    submit = SubmitField('Simpan')

    def validate_tingkat(self, tingkat):
        # Only check uniqueness for new records (logic will be in route/service, 
        # but we can add secondary check here if needed)
        pass
