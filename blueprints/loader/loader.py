from flask import Blueprint, render_template, request, send_from_directory

from sky.hw12.functions import check_file, add_post, save_picture

loader_bp = Blueprint('profile_loader', __name__, static_folder='static', template_folder='templates')


@loader_bp.route('/post/')
def loader_page():
    return render_template("post_form.html")


@loader_bp.route('/post/', methods=['POST'])
def upload():
    content = request.form.get('content')
    picture = request.files.get('picture')
    type_result, result = check_file(picture)
    if type_result:
        picture_path = '/' + save_picture(picture)
        post = add_post({'pic': picture_path, 'content': content})
        return render_template("post_uploaded.html", post=post)
    return result


@loader_bp.route('/uploads/<path:path>')
def upload_page(path):
    return send_from_directory('uploads', path)
