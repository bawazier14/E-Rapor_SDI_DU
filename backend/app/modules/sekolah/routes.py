from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required
from app.modules.sekolah import sekolah_bp
from app.modules.sekolah.forms import SekolahForm
from app.modules.sekolah.services import SekolahService
from app.modules.auth.decorators import roles_required

@sekolah_bp.route('/', methods=['GET', 'POST'])
@login_required
@roles_required('Admin')
def profile():
    sekolah = SekolahService.get_sekolah()
    form = SekolahForm(obj=sekolah)
    
    if form.validate_on_submit():
        SekolahService.update_sekolah(sekolah, request.form, request.files.get('logo'))
        flash('Data sekolah berhasil diperbarui.', 'success')
        return redirect(url_for('sekolah.profile'))
    
    return render_template('sekolah/profile.html', title='Profil Sekolah', sekolah=sekolah, form=form)
