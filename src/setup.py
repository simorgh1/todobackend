from setuptools import setup, find_packages

setup (
  name                 = "todobackend",
  version              = "0.1.1",
  description          = "Todobackend Django REST service",
  packages             = find_packages(),
  include_package_data = True,
  scripts              = ["manage.py"],
  install_requires     = ["Django>=4.0,<4.2",
                          "django-cors-headers>=4.0.0",
                          "djangorestframework>=3.14.0",
                          "MySQL-python>=1.2.5",
                          "uwsgi>=2.0"],
  extras_require       = {
                            "test": [
                              "colorama>=0.3.3",
                              "coverage>=4.0.3",
                              "django-nose>=1.4.2",
                              "nose>=1.3.7",
                              "pinocchio>=0.4.2"
                            ]
                         }
)
