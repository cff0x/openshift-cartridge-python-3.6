from setuptools import setup

setup(name='YourAppName', version='1.0',
      description='OpenShift Python-3.6 Cartridge based application',
      author='Your Name', author_email='ramr@example.org',
      url='http://www.python.org/sigs/distutils-sig/',

      #  Uncomment one or more lines below in the install_requires section
      #  for the specific client drivers/modules your application needs.
      install_requires=['WebOb',
                        #  'mysql-connector-python',
                        #  'pymongo3',
                        #  'psycopg2',
      ],
     )
