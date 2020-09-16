import logging.config
from http import HTTPStatus

from flask import Flask, jsonify

from marshmallow.exceptions import ValidationError

import yaml

from football.config import Config, build_config


def create_app(config_object=Config):
    config_object = build_config(config_object)
    logging.config.dictConfig(yaml.load(open(config_object.LOGGING_CONFIG),
                                        Loader=yaml.FullLoader))
    app = Flask(__name__,
                static_url_path='',
                static_folder='templates/assets',
                template_folder='templates')
    app.config.from_object(config_object)
    logging.info('created app '+str(config_object))
    register_blueprints(app)
    register_errorhandlers(app)
    return app


def register_blueprints(app):
    from football.events.views import blueprints
    app.register_blueprint(blueprints)


def register_errorhandlers(app):
    """Register error handlers."""
    @app.errorhandler(403)
    def handle_forbidden(error):
        return jsonify({'description': error.description}), error.code

    @app.errorhandler(404)
    def handle_not_found(error):
        return jsonify({'description': error.description}), error.code

    @app.errorhandler(422)
    def handle_unprocessable_entity(error):
        response = {
            'description': 'Input failed validation.',
            'errors': error.exc.messages,
        }
        return jsonify(response), HTTPStatus.BAD_REQUEST

    # Catch webargs validation errors and return them in JSON format
    @app.errorhandler(ValidationError)
    def handle_validation_error(error):
        response = {
            'description': 'Input failed validation.',
            'errors': error.messages,
        }
        logging.exception(error)
        return jsonify(response), HTTPStatus.BAD_REQUEST

    @app.errorhandler(UserWarning)
    def handle_userwarning(error):
        logging.exception(error)
        return (jsonify({'description': f'userwarning: {str(error)}'}),
                HTTPStatus.BAD_REQUEST)


app = create_app()
