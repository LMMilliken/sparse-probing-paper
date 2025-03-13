from setuptools import setup, find_packages

setup(
    packages=['sparse_probing_paper.' + pkg for pkg in find_packages(where="sparse_probing_paper")],
)
