from setuptools import setup

setup(name='django_popolo_admin',
      version='0.0.1',
      packages=['popolo_admin'],
      package_data = {'popolo_admin': ['templates/*.html','static/*',],},
      license='MIT',
      author='Ciudadano Inteligente',
      author_email='lab@ciudadanointeligente.org',
      url='https://ciudadanointeligente.org/',
      description='This project adds an admin interface to django_popolo',
      long_description=open("README.md").read(),
      classifiers=[
          'Framework :: Django',
      ],
      install_requires=[
          "Django >= 1.4.3",
          "django-popolo",
      ],
      dependency_links=[
          "https://github.com/openpolis/django-popolo/tarball/master#egg=django-popolo",
          ## It could also be
          ## mysociety-django-popolo
          ## that is already in pypi
      ]
)
