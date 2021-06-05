Starting a new project from an empty folder
====

.. code-block:: bash

    mkdir demo_project
    cd demo_project
    poetry new --src .
    poetry add --dev pre-commit \
                     pytest flake8 mypy \
                     isort black \
                     sphinx
