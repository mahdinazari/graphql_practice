from flask import Blueprint, jsonify
from flask_graphql import GraphQLView

from application.app import create_app
from models.model import schema_query, schema_mutation


blueprint = Blueprint('view', __name__, url_prefix='/api/v1')
app = create_app('application.config.DevelopmentConfig')


@blueprint.route('/main')
def main():
    return jsonify("Hello World")

# Flask Rest & Graphql Routes
@blueprint.route('/graph')
def hello_world():
    return 'Hello From Graphql Tutorial!'


# /graphql-query
blueprint.add_url_rule('/graphql-query', view_func=GraphQLView.as_view(
    'graphql-query',
    schema=schema_query, graphiql=True
))

# /graphql-mutation
blueprint.add_url_rule('/graphql-mutation', view_func=GraphQLView.as_view(
    'graphql-mutation',
    schema=schema_mutation, graphiql=True
))

