simple structure for large flask application
    1.  the config.py: define all config of flask application
    2.  there are 2 environment for configration:
        -   Development Enviroment
        -   Production Environment
    3.  app/__init__.py: Create a Flask application
    4.  app/main/__init__.py: Create a blueprint and import the views, errors, ...
    5.  app/main/view.py: Create a view returns to client       
