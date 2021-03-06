import os
from setuptools import setup, find_packages

ROOT = os.path.abspath(os.path.dirname(__file__))


setup(
    name='django-mobility',
    version='0.1',
    description='Middleware and decorators for directing users to your mobile site.',
    long_description=open(os.path.join(ROOT, 'README.rst')).read(),
    author='Jeff Balogh',
    author_email='jbalogh@mozilla.com',
    url='http://github.com/jbalogh/django-mobility',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['django'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: Mozilla',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
