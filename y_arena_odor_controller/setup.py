import os
from glob import glob
from setuptools import setup

package_name = 'y_arena_odor_controller'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Peter Polidoro',
    author_email='peter@polidoro.io',
    maintainer='Peter Polidoro',
    maintainer_email='peter@polidoro.io',
    description='ROS interface for the Turner Lab Y-Arena rig.',
    keywords=[],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    license='BSD',
    url='https://github.com/janelia-ros/y_arena_odor_controller',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'controller = y_arena_odor_controller.y_arena_odor_controller:main',
            'tester = y_arena_odor_controller.y_arenas_tester:main',
        ],
    },
)
