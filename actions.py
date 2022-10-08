
from flask import Blueprint


# 2)
bp = Blueprint('actions',__name__, url_prefix='/actions')


@bp.route('/resize',methods=["POST"])
def resize():
    pass


@bp.route('/presets/<preset>',methods=["POST"])
def resize_preset(prest):
    pass


@bp.route('/rotate',methods=["POST"])
def rotate_preset():
    pass


@bp.route('/flip',methods=["POST"])
def flip():
    pass