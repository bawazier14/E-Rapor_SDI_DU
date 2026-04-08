from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required
from app.modules.users import users_bp
from app.modules.users.forms import UserCreateForm, UserEditForm, ResetPasswordForm
from app.modules.users.services import UserService
from app.modules.auth.decorators import roles_required

@users_bp.before_request
@login_required
@roles_required('Admin')
def require_admin():
    """Protect all routes in this blueprint to require Admin role."""
    pass

@users_bp.route('/', methods=['GET'])
def index():
    users = UserService.get_all_users()
    return render_template('users/index.html', title='Manajemen Pengguna', users=users)

@users_bp.route('/create', methods=['GET', 'POST'])
def create():
    form = UserCreateForm()
    # Populate choices for roles
    roles = UserService.get_all_roles()
    form.role_id.choices = [(r.id, r.name) for r in roles]

    if form.validate_on_submit():
        data = {
            'username': form.username.data,
            'password': form.password.data,
            'role_id': form.role_id.data,
            'is_active': form.is_active.data
        }
        UserService.create_user(data)
        flash(f'Pengguna {data["username"]} berhasil ditambahkan.', 'success')
        return redirect(url_for('users.index'))

    return render_template('users/create.html', title='Tambah Pengguna', form=form)

@users_bp.route('/<int:user_id>/edit', methods=['GET', 'POST'])
def edit(user_id):
    user = UserService.get_user_by_id(user_id)
    if not user:
        flash('Pengguna tidak ditemukan.', 'danger')
        return redirect(url_for('users.index'))

    form = UserEditForm(original_username=user.username, obj=user)
    roles = UserService.get_all_roles()
    form.role_id.choices = [(r.id, r.name) for r in roles]

    if form.validate_on_submit():
        data = {
            'username': form.username.data,
            'role_id': form.role_id.data,
            'is_active': form.is_active.data
        }
        UserService.update_user(user, data)
        flash(f'Data pengguna {data["username"]} berhasil diperbarui.', 'success')
        return redirect(url_for('users.index'))

    return render_template('users/edit.html', title='Edit Pengguna', form=form, user=user)

@users_bp.route('/<int:user_id>/toggle-status', methods=['POST'])
def toggle_status(user_id):
    user = UserService.get_user_by_id(user_id)
    if not user:
        flash('Pengguna tidak ditemukan.', 'danger')
        return redirect(url_for('users.index'))
    
    if user.username == 'admin':
        flash('Tidak dapat mengubah status Super Admin utama.', 'warning')
    else:
        UserService.toggle_user_status(user)
        status_text = "diaktifkan" if user.is_active else "dinonaktifkan"
        flash(f'Akun {user.username} telah {status_text}.', 'info')
        
    return redirect(url_for('users.index'))

@users_bp.route('/<int:user_id>/reset-password', methods=['GET', 'POST'])
def reset_password(user_id):
    user = UserService.get_user_by_id(user_id)
    if not user:
        flash('Pengguna tidak ditemukan.', 'danger')
        return redirect(url_for('users.index'))

    form = ResetPasswordForm()
    if form.validate_on_submit():
        UserService.reset_password(user, form.password.data)
        flash(f'Password untuk {user.username} berhasil direset.', 'success')
        return redirect(url_for('users.index'))

    return render_template('users/reset_password.html', title='Reset Password', form=form, user=user)
