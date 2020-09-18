
from flask import Blueprint, jsonify, render_template

from webargs import fields
from webargs.flaskparser import use_args

from football.events.spread_analyzer import combined_spreads


blueprints = Blueprint('blueprints', __name__)


@blueprints.route('/')
def builder():
    return render_template('index.html')


event_args = {
    'from_date': fields.Str(required=True),
    'to_date': fields.Str(required=True),
 }


@blueprints.route('/events', methods=['GET'])
@use_args({'from_date': fields.Str(required=True),
           'to_date': fields.Str(required=True)}, location='query')
def get_designs(args):
    data = combined_spreads(args.get('from_date'),
                            args.get('to_date'))
    return jsonify(data)
