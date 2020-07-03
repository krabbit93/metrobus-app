import os
from flask import Flask
from flask_graphql import GraphQLView
from api import schema
app = Flask(__name__)


if __name__ == "__main__":
    app.add_url_rule("/api", view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    ))
    app.run(host="0.0.0.0")
