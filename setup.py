#!/usr/bin/env python

from distutils.core import setup

setup(
    name="IntFicPy Qt GUI",
    version="0.1.1",
    description="A GUI for IntFicPy games, implemented with PyQt5",
    author="JSMaika",
    author_email="r.a.lester121@gmail.com",
    py_modules=['ifp_qt_gui'],
    install_requires=["PyQt5"],  # external packages as dependencies
)
