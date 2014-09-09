from setuptools import setup

setup(name='django_popolo_admin',
      version='0.0.1',
      packages=['django_popolo_admin'],
      package_data = {'django_popolo_admin': ['templates/*.html','static/*',],},
      license='MIT',
      author='Ciudadano Inteligente',
      author_email='lab@ciudadanointeligente.org',
      url='https://ciudadanointeligente.org/',
      description='This project adds an admin interface to django_popolo',
      long_description=open("README.md").read(),
      install_requires=['Django >= 1.4.3'],
      classifiers=[
          'Framework :: Django',
      ],
)
