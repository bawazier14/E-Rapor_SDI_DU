from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required
from app.modules.siswa import siswa_bp
from app.modules.siswa.services import SiswaService
from app.modules.siswa.forms import SiswaForm
from app.modules.auth.decorators import roles_required

@siswa_bp.route('/')
@login_required
@roles_required('Admin')
def index():
    siswas = SiswaService.get_all_siswa()
    return render_template('siswa/index.html', siswas=siswas, title='Daftar Siswa')

@siswa_bp.route('/create', methods=['GET', 'POST'])
@login_required
@roles_required('Admin')
def create():
    form = SiswaForm()
    if form.validate_on_submit():
        SiswaService.create_siswa(form.data)
        flash('Data siswa berhasil ditambahkan!', 'success')
        return redirect(url_for('siswa.index'))
    return render_template('siswa/create.html', form=form, title='Tambah Siswa')

@siswa_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
@roles_required('Admin')
def edit(id):
    siswa = SiswaService.get_siswa_by_id(id)
    if not siswa:
        flash('Data siswa tidak ditemukan!', 'danger')
        return redirect(url_for('siswa.index'))
    
    form = SiswaForm(obj=siswa)
    if form.validate_on_submit():
        SiswaService.update_siswa(siswa, form.data)
        flash('Data siswa berhasil diperbarui!', 'success')
        return redirect(url_for('siswa.index'))
    
    return render_template('siswa/edit.html', form=form, siswa=siswa, title='Edit Siswa')

@siswa_bp.route('/delete/<int:id>', methods=['POST'])
@login_required
@roles_required('Admin')
def delete(id):
    siswa = SiswaService.get_siswa_by_id(id)
    if not siswa:
        flash('Data siswa tidak ditemukan!', 'danger')
        return redirect(url_for('siswa.index'))
    
    SiswaService.delete_siswa(siswa)
    flash('Data siswa berhasil dihapus!', 'warning')
    return redirect(url_for('siswa.index'))
