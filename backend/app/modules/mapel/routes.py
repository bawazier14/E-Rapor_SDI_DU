from flask import render_template, redirect, url_for, flash, request
from app.modules.mapel import mapel_bp
from app.modules.mapel.services import MapelService
from app.modules.mapel.forms import MapelForm
from app.modules.auth.decorators import roles_required
from flask_login import login_required

@mapel_bp.route('/')
@login_required
@roles_required('Admin')
def index():
    mapels = MapelService.get_all_mapel()
    return render_template('mapel/index.html', mapels=mapels)

@mapel_bp.route('/create', methods=['GET', 'POST'])
@login_required
@roles_required('Admin')
def create():
    form = MapelForm()
    if form.validate_on_submit():
        try:
            MapelService.create_mapel(form.data)
            flash('Mata Pelajaran berhasil ditambahkan!', 'success')
            return redirect(url_for('mapel.index'))
        except ValueError as e:
            flash(str(e), 'danger')
            
    return render_template('mapel/create.html', form=form)

@mapel_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
@roles_required('Admin')
def edit(id):
    mapel = MapelService.get_mapel_by_id(id)
    form = MapelForm(obj=mapel)
    
    if form.validate_on_submit():
        try:
            MapelService.update_mapel(id, form.data)
            flash('Mata Pelajaran berhasil diperbarui!', 'success')
            return redirect(url_for('mapel.index'))
        except ValueError as e:
            flash(str(e), 'danger')
            
    return render_template('mapel/edit.html', form=form, mapel=mapel)

@mapel_bp.route('/delete/<int:id>', methods=['POST'])
@login_required
@roles_required('Admin')
def delete(id):
    try:
        MapelService.delete_mapel(id)
        flash('Mata Pelajaran berhasil dihapus!', 'success')
    except ValueError as e:
        flash(str(e), 'danger')
        
    return redirect(url_for('mapel.index'))
