import os
import subprocess

import flask
from flask import request, flash, redirect, url_for, send_from_directory, render_template, send_file
from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms.fields.form import FormField
from werkzeug.utils import secure_filename
import threading

from data.history import History
from data import db_session

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = '23456fusaftdr68fty32hhwftr6tyJBHFY&RtqgevgutiOHOPU_$$UnWDjk'

UPLOAD_FOLDER = 'C:\\PycharmProjects\\Verconter\\uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

first_file = ''
second_file = ''


def task(filename):
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

                subprocess.call("mp4_to_avi.sh")
                return f'{filename.rsplit('.', 1)[0]}.avi'
            elif second_file == 'gif':
                abs_folder = os.path.abspath('uploads')
                batch_content_small = f"""
                                                            cd {abs_folder}
                                                            ffmpeg -i "{filename}" -t 10 "{filename.rsplit('.', 1)[0]}.gif"
                                                            """

                with open("mp4_to_gif.sh", "w+") as file:
                    file.write(batch_content_small)

                subprocess.call("mp4_to_gif.sh")
                return f'{filename.rsplit('.', 1)[0]}.gif'
            elif second_file == 'mp3':
                abs_folder = os.path.abspath('uploads')
                batch_content_small = f"""
                                                cd {abs_folder}
                                                ffmpeg -i "{filename}" -map 0:1 "{filename.rsplit('.', 1)[0]}.mp3"
                                                """

                with open("mp4_to_mp3.sh", "w+") as file:
                    file.write(batch_content_small)

                subprocess.call("mp4_to_mp3.sh")
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

                subprocess.call("mp3_to_ogg.sh")
                return f'{filename.rsplit('.', 1)[0]}.ogg'
            elif second_file == 'wav':
                abs_folder = os.path.abspath('uploads')
                batch_content_small = f"""
                                                cd {abs_folder}
                                                ffmpeg -i "{filename}" "{filename.rsplit('.', 1)[0]}.wav"
                                                """

                with open("mp3_to_wav.sh", "w+") as file:
                    file.write(batch_content_small)

                subprocess.call("mp3_to_wav.sh")
                return f'{filename.rsplit('.', 1)[0]}.wav'
            elif second_file == 'm4a':
                abs_folder = os.path.abspath('uploads')
                batch_content_small = f"""
                                                cd {abs_folder}
                                                ffmpeg -i "{filename}" "{filename.rsplit('.', 1)[0]}.m4a"
                                                """

                with open("mp3_to_m4a.sh", "w+") as file:
                    file.write(batch_content_small)

                subprocess.call("mp3_to_m4a.sh")
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

                subprocess.call("png_to_jpg.sh")
                return f'{filename.rsplit('.', 1)[0]}.jpg'



class SelectForm(FlaskForm):
    type_ = first_choise = SelectField('First file', choices=[('mp4', '.mp4'), ('mp3', '.mp3'), ('png', '.png')])
    type_mp4 = second_choise_mp4 = SelectField('Second file', choices=[('avi', '.avi'),('mp3', '.mp3'), ('gif', '.gif (первые 10 сек)')])
    type_mp3 = second_choise_mp3 = SelectField('Second file',
                                               choices=[('ogg', '.ogg'), ('wav', '.wav'), ('m4a', '.m4a')])
    type_png = second_choise_txt = SelectField('Second file',
                                               choices=[('jpg', '.jpg')])



class MyForm(FlaskForm):
    select = FormField(SelectForm)


@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('main.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in first_file


@app.route('/history')
def history():
    db_sess = db_session.create_session()
    history1 = db_sess.query(History).all()
    db_sess.commit()
    return flask.render_template('history.html', history=history1)


@app.route('/converter', methods =["GET", "POST"])
def converter():
    if os.name == 'nt':
        os.system('del /Q C:\\PycharmProjects\\Verconter\\uploads')
        os.system('mkdir C:\\PycharmProjects\\Verconter\\uploads')
    return redirect('/converter_first')


@app.route('/converter_first', methods=['GET', 'POST'])
def conv1():
    global first_file
    form = MyForm()
    if request.method == 'POST':
        first_file = form.select.type_.data
        return redirect('/converter_second')
    return render_template('converter1.html', form=form)


@app.route('/converter_second', methods=['GET', 'POST'])
def conv2():
    global second_file
    form = MyForm()
    if request.method == 'POST':
        if first_file == 'mp4':
            second_file = form.select.type_mp4.data
        elif first_file == 'mp3':
            second_file = form.select.type_mp3.data
        elif first_file == 'png':
            second_file = form.select.type_png.data
        return redirect('/converter_finish')
    return render_template('converter2.html', form=form, first_file=first_file)


@app.route('/converter_finish', methods=['GET', 'POST'])
def conv_finish():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Неверный формат файла', 'error')
        file = request.files['file']
        if file.filename == '':
            flash('Не выбран файл', 'error')
        if not allowed_file(file.filename):
            flash('Неверный формат файла', 'error')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            if len(filename.rsplit('.', 1)) == 1:
                filename = 'asdasd.' + filename.rsplit('.', 1)[-1]
            flash('Успех')
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(f'/converter_download/{filename}')

    return render_template('converter.html')


@app.route('/converter_download/<name_of_file>', methods=['GET', 'POST'])
def converter_last(name_of_file):
    if request.method == 'POST':
        name = task(name_of_file)
        return redirect(f'/uploads/{name}')
    return render_template('converter_last.html')


@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)


@app.route('/images/<imagename>')
def image(imagename):
    a = os.getcwd() + f'/images/{imagename}'
    return flask.send_file(a)


@app.route('/<filename>')
def get_file(filename):
    a = os.getcwd() + f'/images/{filename}'
    return flask.send_file(a)


def main():
    db_session.global_init("database/history.db")
    port = int(os.environ.get("PORT", 5000))
    app.run(port=port, host='0.0.0.0')


if __name__ == '__main__':
    main()
