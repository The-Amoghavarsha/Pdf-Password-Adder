from setuptools import setup, find_packages

setup(
    name='pdf_password_adder',
    version='1.0.0',
    description='A tool for adding passwords to PDF files',
    url='https://github.com/the-amoghavarsha/pdf-password-adder',
    author='Amoghavarsha',
    author_email='amoghavarsha004@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=["qpdf"],
    entry_points={
        'console_scripts': [
            'pdf_password_adder = pdf_password_adder.pdf_password_adder:main'
        ]
    },
)

