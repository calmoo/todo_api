from setuptools import find_packages, setup

setup(
    name="todo_app",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "Flask==1.1.2",
        "SQLAlchemy==1.3.19",
        "argon2-cffi",
        "Flask-JWT-Extended==3.24.1",
    ],
)
