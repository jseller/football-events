
from flask import Blueprint, jsonify, render_template, request

from webargs import fields
from webargs.flaskparser import parser

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
def get_designs():
    args = parser.parse(event_args, request)
    data = combined_spreads(args.get('from_date'),
                            args.get('to_date'))
    return jsonify({'success': 'updated now ', 'data': data})
