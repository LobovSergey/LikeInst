from flask import Blueprint, render_template, request

from sky.hw12.functions import load_json

main_bp = Blueprint('profile_main', __name__, static_folder='static', template_folder='templates')


@main_bp.route('/')
def main_page():
    return render_template("index.html")


@main_bp.route("/search/", methods=["GET"])
def page_tag():
    tag = request.args.get('s', '')
    post_list = load_json()
    return render_template("post_list.html", tag=tag, post_list=post_list)
