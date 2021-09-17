from setuptools import setup

package_name = 'y_arena_python_pub'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='peter@polidoro.io',
    description='Example Python publisher for Turner Lab Y-Arena rig.',
    license='BSD',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'y_arena_python_pub = y_arena_python_pub.y_arena_python_pub:main'
        ],
    },
)
