from flask import Blueprint, render_template

blueprint = Blueprint('setup', __name__)


@blueprint.route('/setup')
def setup():
    return render_template('setup.html')
