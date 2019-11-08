from setuptools import setup

setup(
    name='trackhub-nominatim',
    version='0.1.0',
    packages=['nominatim', 'nominatim.formatters', 'nominatim.validators'],
    url='https://github.com/trackhub/trackhub-nominatim',
    license='MIT',
    author='stefan',
    author_email='stefan.mavrodiev@gmail.com',
    description='Export countries from nominatim service'
)
