from setuptools import find_packages, setup

package_name = 'opencv_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vi',
    maintainer_email='vi@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'cv_tx_node = opencv_pkg.opencv_0:main',
            'cv_rx_node = opencv_pkg.opencv_0_rx:main',
            
            'cv_new_tx_node = opencv_pkg.opencv_1_tx:main',
            'cv_new_rx_node = opencv_pkg.opencv_1_rx:main',
        ],
    },
)
