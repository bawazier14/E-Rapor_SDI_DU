from flask import render_template, redirect, url_for, flash, request
from app.modules.kelas import kelas_bp
from app.modules.kelas.services import KelasService
from app.modules.kelas.forms import KelasForm
from app.modules.auth.decorators import roles_required
from flask_login import login_required

@kelas_bp.route('/')
@login_required
@roles_required('Admin')
def index():
    kelasList = KelasService.get_all_kelas()
    return render_template('kelas/index.html', kelasList=kelasList)

@kelas_bp.route('/create', methods=['GET', 'POST'])
@login_required
@roles_required('Admin')
def create():
    form = KelasForm()
    if form.validate_on_submit():
        try:
            KelasService.create_kelas(form.data)
            flash('Tingkat kelas berhasil ditambahkan!', 'success')
            return redirect(url_for('kelas.index'))
        except ValueError as e:
            flash(str(e), 'danger')
            
    return render_template('kelas/create.html', form=form)

@kelas_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
@roles_required('Admin')
def edit(id):
    kelas = KelasService.get_kelas_by_id(id)
    form = KelasForm(obj=kelas)
    
    if form.validate_on_submit():
        try:
            KelasService.update_kelas(id, form.data)
            flash('Tingkat kelas berhasil diperbarui!', 'success')
            return redirect(url_for('kelas.index'))
        except ValueError as e:
            flash(str(e), 'danger')
            
    return render_template('kelas/edit.html', form=form, kelas=kelas)

@kelas_bp.route('/delete/<int:id>', methods=['POST'])
@login_required
@roles_required('Admin')
def delete(id):
    try:
        KelasService.delete_kelas(id)
        flash('Tingkat kelas berhasil dihapus!', 'success')
    except ValueError as e:
        flash(str(e), 'danger')
        
    return redirect(url_for('kelas.index'))
