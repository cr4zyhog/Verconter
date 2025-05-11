import os
import subprocess
import datetime

import flask
from flask import request, flash, redirect, url_for, send_from_directory, render_template, send_file, make_response, \
    jsonify

from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms.fields.form import FormField
from werkzeug.utils import secure_filename

from data.history import History
from data.users import User
from data.register import RegisterForm
from data.login import LoginForm
from data import db_session

app = flask.Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = '23456fusaftdr68fty32hhwftr6tyJBHFY&RtqgevgutiOHOPU_$$UnWDjk'

if os.name == 'nt':
    UPLOAD_FOLDER = 'C:\\PycharmProjects\\Verconter\\uploads'
    ICON_FOLDER = 'C:\\PycharmProjects\\Verconter\\icons'
else:
    UPLOAD_FOLDER = '/home/Verconter/uploads'
    ICON_FOLDER = '/home/Verconter/icons'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ICON_FOLDER'] = ICON_FOLDER

files = []

login_manager = LoginManager()
login_manager.init_app(app)


def task(filename, *types):
    print(types)
    first_file = types[0]
    second_file = types[1]
    if os.name == 'nt':
        if first_file == 'mp4':
            if second_file == 'avi':
                abs_folder = os.path.abspath('uploads')
                batch_content_small = f"""
                                            cd {abs_folder}
                                            ffmpeg -i "{filename}" "{filename.rsplit('.', 1)[0]}.avi"
                                            """

                with open("mp4_to_avi.bat", "w+") as file:
                    file.write(batch_content_small)

                subprocess.call("mp4_to_avi.bat")
                return f'{filename.rsplit('.', 1)[0]}.avi'
            elif second_file == 'gif':
                abs_folder = os.path.abspath('uploads')
                batch_content_small = f"""
                                                            cd {abs_folder}
                                                            ffmpeg -i "{filename}" -t 10 "{filename.rsplit('.', 1)[0]}.gif"
                                                            """

                with open("mp4_to_gif.bat", "w+") as file:
                    file.write(batch_content_small)

                subprocess.call("mp4_to_gif.bat")
                return f'{filename.rsplit('.', 1)[0]}.gif'
            elif second_file == 'mp3':
                abs_folder = os.path.abspath('uploads')
                batch_content_small = f"""
                                                cd {abs_folder}
                                                ffmpeg -i "{filename}" -map 0:1 "{filename.rsplit('.', 1)[0]}.mp3"
                                                """

                with open("mp4_to_mp3.bat", "w+") as file:
                    file.write(batch_content_small)

                subprocess.call("mp4_to_mp3.bat")
                return f'{filename.rsplit('.', 1)[0]}.mp3'
        elif first_file == 'mp3':
            if second_file == 'ogg':
                abs_folder = os.path.abspath('uploads')
                batch_content_small = f"""
                                                cd {abs_folder}
                                                ffmpeg -i "{filename}" "{filename.rsplit('.', 1)[0]}.ogg"
                                                """

                with open("mp3_to_ogg.bat", "w+") as file:
                    file.write(batch_content_small)

                subprocess.call("mp3_to_ogg.bat")
                return f'{filename.rsplit('.', 1)[0]}.ogg'
            elif second_file == 'wav':
                abs_folder = os.path.abspath('uploads')
                batch_content_small = f"""
                                                cd {abs_folder}
                                                ffmpeg -i "{filename}" "{filename.rsplit('.', 1)[0]}.wav"
                                                """

                with open("mp3_to_wav.bat", "w+") as file:
                    file.write(batch_content_small)

                subprocess.call("mp3_to_wav.bat")
                return f'{filename.rsplit('.', 1)[0]}.wav'
            elif second_file == 'm4a':
                abs_folder = os.path.abspath('uploads')
                batch_content_small = f"""
                                                cd {abs_folder}
                                                ffmpeg -i "{filename}" "{filename.rsplit('.', 1)[0]}.m4a"
                                                """

                with open("mp3_to_m4a.bat", "w+") as file:
                    file.write(batch_content_small)

                subprocess.call("mp3_to_m4a.bat")
                return f'{filename.rsplit('.', 1)[0]}.m4a'
        elif first_file == 'png':
            if second_file == 'jpg':
                abs_folder = os.path.abspath('uploads')
                batch_content_small = f"""
                                                cd {abs_folder}
                                                ffmpeg -i "{filename}" "{filename.rsplit('.', 1)[0]}.jpg"
                                                """

                with open("png_to_jpg.bat", "w+") as file:
                    file.write(batch_content_small)

                subprocess.call("png_to_jpg.bat")
                return f'{filename.rsplit('.', 1)[0]}.jpg'
    elif os.name == 'posix':
        if first_file == 'mp4':
            if second_file == 'avi':
                abs_folder = os.path.abspath('uploads')
                batch_content_small = f"""
                                            cd {abs_folder}
                                            ffmpeg -i "{filename}" "{filename.rsplit('.', 1)[0]}.avi"
                                            """

                with open("mp4_to_avi.sh", "w+") as file:
                    file.write(batch_content_small)

                subprocess.call("chmod u+r+x ./mp4_to_avi.sh; ./mp4_to_avi.sh", shell=True)
                return f'{filename.rsplit('.', 1)[0]}.avi'
            elif second_file == 'gif':
                abs_folder = os.path.abspath('uploads')
                batch_content_small = f"""
                                                            cd {abs_folder}
                                                            ffmpeg -i "{filename}" -t 10 "{filename.rsplit('.', 1)[0]}.gif"
                                                            """

                with open("mp4_to_gif.sh", "w+") as file:
                    file.write(batch_content_small)

                subprocess.call("chmod u+r+x ./mp4_to_gif.sh; ./mp4_to_gif.sh", shell=True)
                return f'{filename.rsplit('.', 1)[0]}.gif'
            elif second_file == 'mp3':
                abs_folder = os.path.abspath('uploads')
                batch_content_small = f"""
                                                cd {abs_folder}
                                                ffmpeg -i "{filename}" -map 0:1 "{filename.rsplit('.', 1)[0]}.mp3"
                                                """

                with open("mp4_to_mp3.sh", "w+") as file:
                    file.write(batch_content_small)

                subprocess.call("chmod u+r+x ./mp4_to_mp3.sh; ./mp4_to_mp3.sh", shell=True)
                return f'{filename.rsplit('.', 1)[0]}.mp3'
        elif first_file == 'mp3':
            if second_file == 'ogg':
                abs_folder = os.path.abspath('uploads')
                batch_content_small = f"""
                                                cd {abs_folder}
                                                ffmpeg -i "{filename}" "{filename.rsplit('.', 1)[0]}.ogg"
                                                """

                with open("mp3_to_ogg.sh", "w+") as file:
                    file.write(batch_content_small)

                subprocess.call("chmod u+r+x ./mp3_to_ogg.sh; ./mp3_to_ogg.sh", shell=True)
                return f'{filename.rsplit('.', 1)[0]}.ogg'
            elif second_file == 'wav':
                abs_folder = os.path.abspath('uploads')
                batch_content_small = f"""
                                                cd {abs_folder}
                                                ffmpeg -i "{filename}" "{filename.rsplit('.', 1)[0]}.wav"
                                                """

                with open("mp3_to_wav.sh", "w+") as file:
                    file.write(batch_content_small)

                subprocess.call("chmod u+r+x ./mp3_to_wav.sh; ./mp3_to_wav.sh", shell=True)
                return f'{filename.rsplit('.', 1)[0]}.wav'
            elif second_file == 'm4a':
                abs_folder = os.path.abspath('uploads')
                batch_content_small = f"""
                                                cd {abs_folder}
                                                ffmpeg -i "{filename}" "{filename.rsplit('.', 1)[0]}.m4a"
                                                """

                with open("mp3_to_m4a.sh", "w+") as file:
                    file.write(batch_content_small)

                subprocess.call("chmod u+r+x ./mp3_to_m4a.sh; ./mp3_to_m4a.sh", shell=True)
                return f'{filename.rsplit('.', 1)[0]}.m4a'
        elif first_file == 'png':
            if second_file == 'jpg':
                abs_folder = os.path.abspath('uploads')
                batch_content_small = f"""
                                                cd {abs_folder}
                                                ffmpeg -i "{filename}" "{filename.rsplit('.', 1)[0]}.jpg"
                                                """

                with open("png_to_jpg.sh", "w+") as file:
                    file.write(batch_content_small)

                subprocess.call("chmod u+r+x ./png_to_jpg.sh; ./png_to_jpg.sh", shell=True)
                return f'{filename.rsplit('.', 1)[0]}.jpg'


class SelectForm(FlaskForm):
    type_ = first_choise = SelectField('First file', choices=[('mp4', '.mp4'), ('mp3', '.mp3'), ('png', '.png')])
    type_mp4 = second_choise_mp4 = SelectField('Second file', choices=[('avi', '.avi'), ('mp3', '.mp3'),
                                                                       ('gif', '.gif (первые 10 сек)')])
    type_mp3 = second_choise_mp3 = SelectField('Second file',
                                               choices=[('ogg', '.ogg'), ('wav', '.wav'), ('m4a', '.m4a')])
    type_png = second_choise_txt = SelectField('Second file',
                                               choices=[('jpg', '.jpg')])


class MyForm(FlaskForm):
    select = FormField(SelectForm)


@login_manager.user_loader
def load_user(user_id):
    print(user_id)
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('main.html')


def allowed_file(filename, type1):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in type1


def allowed_file2(filename, types):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in types


@app.route('/history')
def history():
    db_sess = db_session.create_session()
    try:
        a = db_sess.query(User).filter(User.id == current_user.id)[0].history.split(',')
        history1 = db_sess.query(History).filter(History.id.in_(a)).all()
        db_sess.commit()
    except AttributeError:
        history1 = ['a']
    return flask.render_template('history.html', history=history1)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('signin.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('signin.html', title='Авторизация', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User()
        db_sess = db_session.create_session()
        user.login = form.login.data
        user.email = form.email.data
        user.set_password(form.password.data)
        user.history = ''
        user.image = None
        db_sess.add(user)
        try:
            db_sess.commit()
        except Exception as e:
            return render_template('signup.html',
                                   title='Регистрация',
                                   form=form,
                                   message="Уже есть")
        return redirect("/signin")
    return render_template('signup.html', title='Регистрация', form=form)


@app.route('/converter', methods=["GET", "POST"])
def converter():
    if os.name == 'nt':
        for i in files:
            os.system(f'del /Q C:\\PycharmProjects\\Verconter\\uploads\\{i}')
    elif os.name == 'posix':
        for i in files:
            os.system(f'rm -f -r /home/Verconter/uploads\\{i}')
    return redirect('/converter_first')


@app.route('/converter_first', methods=['GET', 'POST'])
def conv1():
    form = MyForm()
    if request.method == 'POST':
        return redirect(f'/converter_second/{form.select.type_.data}')
    return render_template('converter1.html', form=form)


@app.route('/converter_second/<type1>', methods=['GET', 'POST'])
def conv2(type1):
    form = MyForm()
    if request.method == 'POST':
        if type1 == 'mp4':
            return redirect(f'/converter_finish/{type1}/{form.select.type_mp4.data}')
        elif type1 == 'mp3':
            return redirect(f'/converter_finish/{type1}/{form.select.type_mp3.data}')
        elif type1 == 'png':
            return redirect(f'/converter_finish/{type1}/{form.select.type_png.data}')
    return render_template('converter2.html', form=form, first_file=type1)


@app.route('/converter_finish/<type1>/<type2>', methods=['GET', 'POST'])
def conv_finish(type1, type2):
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Неверный формат файла', 'error')
        file = request.files['file']
        if file.filename == '':
            flash('Не выбран файл', 'error')
        if not allowed_file(file.filename, type1):
            flash('Неверный формат файла', 'error')
        if file and allowed_file(file.filename, type1):
            filename = secure_filename(file.filename)
            if len(filename.rsplit('.', 1)) == 1:
                filename = 'asdasd.' + filename.rsplit('.', 1)[-1]
            flash('Успех')
            files.append(filename)
            files.append(filename.rsplit('.', 1)[0] + '.' + type2)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            history11 = History()
            db_sess = db_session.create_session()
            ta = datetime.datetime.now()
            history11.date = ta
            history11.file = filename
            history11.res_file = filename.rsplit('.', 1)[0] + '.' + type2
            db_sess.add(history11)
            db_sess.commit()
            db_sess = db_session.create_session()

            a = db_sess.query(User).filter(User.id == current_user.id)[0].history.split(',')
            b = db_sess.query(History).filter(History.file == filename)[0]
            if b.res_file == filename.rsplit('.', 1)[0] + '.' + type2:
                a.append(str(b.id))
                print(a)
                ai = db_sess.query(User).filter(User.id == current_user.id)[0]
                ai.history = ','.join(a)
                db_sess.add(ai)
                db_sess.commit()
            return redirect(f'/converter_download/{filename}/{type1}/{type2}')

    return render_template('converter.html')


@app.route('/converter_download/<name_of_file>/<type1>/<type2>', methods=['GET', 'POST'])
def converter_last(name_of_file, type1, type2):
    if request.method == 'POST':
        name = task(name_of_file, type1, type2)
        return redirect(f'/uploads/{name}')
    return render_template('converter_last.html')


@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)


@app.route('/images/<imagename>')
def image(imagename):
    a = os.getcwd() + f'/images/{imagename}'
    return flask.send_file(a)


@app.route('/styles/<name>')
def stylessss(name):
    a = os.getcwd() + f'/styles/{name}'
    return flask.send_file(a)


@app.route('/<filename>')
def get_file(filename):
    try:
        a = os.getcwd() + f'/images/{filename}'
        return flask.send_file(a)
    except FileNotFoundError:
        return render_template('404.html')


@app.route('/icons/<filename>')
def get_icon(filename):
    a = os.getcwd() + f'/icons/{filename}'
    return flask.send_file(a)


@app.route('/profile')
def profile():
    if current_user.is_authenticated:
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.id == current_user.id)[0]
        icon = user.image
        if icon == None:
            icon = 'icons/base_image_icon_verconter_nikto_ne_napishet_eto_nazvaniyeghfdjgsaftydqutwte76uqdfyafusyfuydafuywdfqyusafdfaYUDfuasfdiyudsafd.png'
        return render_template('profile.html', loginn=user.login, source=icon)
    else:
        return render_template('profile.html')


@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    if current_user.is_authenticated:
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.id == current_user.id)[0]
        if request.method == 'POST':
            if 'file' not in request.files:
                flash('ошибка', 'error')
            file = request.files['file']
            naaameee = request.form['new_name']
            if file.filename == '':
                flash('Не выбран файл', 'error')
            if not allowed_file2(file.filename, ['png', 'jpg', 'gif']):
                flash('Неверный формат файла(можно только .png, .jpg и .gif)', 'error')
            if file and allowed_file2(file.filename, ['png', 'jpg', 'gif']):
                filename = secure_filename(file.filename)
                if len(filename.rsplit('.', 1)) == 1:
                    filename = 'asdasd.' + filename.rsplit('.', 1)[-1]
                flash('Успех')
                file.save(os.path.join(app.config['ICON_FOLDER'], filename))
                old_im = user.image

                user.image = f'icons/{filename}'
                user.login = naaameee
                db_sess.add(user)
                db_sess.commit()
                if os.name == 'nt':
                    os.remove(f'C:/PycharmProjects/Verconter/{old_im}')
                elif os.name == 'posix':
                    os.remove(f'/home/Verconter/{old_im}')
                return redirect('/profile')
        return render_template('edit_profile.html', loginn=user.login)
    else:
        return render_template('edit_profile.html',)


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


@app.errorhandler(404)
def bad_requesst(_):
    return render_template('404.html')


def main():
    db_session.global_init("database/history.db")
    port = int(os.environ.get("PORT", 5000))
    app.run(port=port, host='0.0.0.0')


if __name__ == '__main__':
    main()
