from setuptools import setup
'''
add the CLI to scrips
pip install --editable
'''
setup(
    name='mycli',
    version='1.0',
    py_modules=['mycli'],
    install_require=['Click', 'colorama'],
    entry_points='''
        [console_scripts]
        mycli=mycli:hello
    ''',
)
