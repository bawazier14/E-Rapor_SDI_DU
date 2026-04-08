from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required
from app.modules.guru import guru_bp
from app.modules.guru.forms import GuruForm
from app.modules.guru.services import GuruService
from app.modules.auth.decorators import roles_required

@guru_bp.route('/')
@login_required
@roles_required('Admin')
def index():
    gurus = GuruService.get_all_guru()
    return render_template('guru/index.html', title='Data Guru', gurus=gurus)

@guru_bp.route('/create', methods=['GET', 'POST'])
@login_required
@roles_required('Admin')
def create():
    form = GuruForm()
    if form.validate_on_submit():
        GuruService.create_guru(form.data, create_user=form.create_user.data)
        flash('Data guru berhasil ditambahkan.', 'success')
        return redirect(url_for('guru.index'))
    return render_template('guru/create.html', title='Tambah Guru', form=form)

@guru_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
@login_required
@roles_required('Admin')
def edit(id):
    guru = GuruService.get_guru_by_id(id)
    if not guru:
        flash('Data guru tidak ditemukan.', 'danger')
        return redirect(url_for('guru.index'))
    
    form = GuruForm(obj=guru)
    if form.validate_on_submit():
        GuruService.update_guru(guru, form.data, sync_user=form.create_user.data)
        flash('Data guru berhasil diperbarui.', 'success')
        return redirect(url_for('guru.index'))
    
    # Pre-select create_user if user already exists
    if request.method == 'GET':
        form.create_user.data = True if guru.user else False
        
    return render_template('guru/edit.html', title='Edit Guru', form=form, guru=guru)

@guru_bp.route('/<int:id>/toggle-status', methods=['POST'])
@login_required
@roles_required('Admin')
def toggle_status(id):
    guru = GuruService.get_guru_by_id(id)
    if not guru:
        flash('Data guru tidak ditemukan.', 'danger')
        return redirect(url_for('guru.index'))
    
    GuruService.toggle_guru_status(guru)
    flash(f'Status {guru.nama_lengkap} berhasil diubah.', 'success')
    return redirect(url_for('guru.index'))
