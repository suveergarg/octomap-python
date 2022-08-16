import subprocess
import sys
from setuptools import Extension
from setuptools import setup
import os

def get_long_description():
    with open('README.md') as f:
        long_description = f.read()
    return long_description

from Cython.Distutils import build_ext
import numpy

os.makedirs('src/octomap/build', exist_ok=True)
subprocess.run(['cmake', ".."], cwd='src/octomap/build', check=True)
subprocess.run(['make'], cwd='src/octomap/build', check=True)

ext_modules = [
    Extension(
        'octomap',
        ['octomap/octomap.pyx'],
        include_dirs=[
            'src/octomap/octomap/include',
            'src/octomap/dynamicEDT3D/include',
            numpy.get_include(),
        ],
        language='c++',
        extra_objects=[
            "src/octomap/lib/libdynamicedt3d.a",
            "src/octomap/lib/liboctomap.a",
            "src/octomap/lib/liboctomath.a",
            "src/octomap/lib/liboctovis.a",
        ]
    )
]

setup(
    name='octomap-python',
    version='1.8.0.post12',
    install_requires=['numpy'],
    extras_require={
        'example': ['glooey', 'imgviz', 'pyglet', 'trimesh[easy]'],
    },
    license='BSD',
    maintainer='Suveer Garg',
    maintainer_email='suveer.garg@samsung.com',
    url='https://github.com/gsuveer/octomap-python',
    ext_modules=ext_modules,
    cmdclass={'build_ext': build_ext},
)

