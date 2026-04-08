from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, logout_user, login_required
from urllib.parse import urlparse

from app.modules.auth import auth_bp
from app.modules.auth.forms import LoginForm
from app.modules.auth.services import AuthService

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard_tmp')) # Assuming a dashboard module

    form = LoginForm()
    if form.validate_on_submit():
        user = AuthService.authenticate_user(form.username.data, form.password.data)
        if user is None:
            flash('Username atau password tidak valid, atau akun tidak aktif.', 'danger')
            return redirect(url_for('auth.login'))
        
        login_user(user, remember=form.remember_me.data)
        
        next_page = request.args.get('next')
        if not next_page or urlparse(next_page).netloc != '':
            next_page = url_for('dashboard_tmp') # TODO: create dashboard route
            
        return redirect(next_page)
        
    return render_template('auth/login.html', title='Sign In', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Anda telah berhasil keluar dari sistem.', 'info')
    return redirect(url_for('auth.login'))
