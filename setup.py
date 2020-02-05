from setuptools import setup, find_packages
from distutils.extension import Extension

try:
    from Cython.Build import cythonize
    extension = cythonize([Extension('packbits._packbits', ['src/packbits/_packbits.pyx'])])
except ImportError:
    extension = [Extension('packbits._packbits', ['src/packbits/_packbits.c'])]


setup(
    name='packbits',
    version='0.7',
    author='Kota Yamaguchi',
    author_email='KotaYamaguchi1984@gmail.com',
    url='https://github.com/psd-tools/packbits',
    description='PackBits encoder/decoder',
    long_description=open('README.rst').read(),
    license='MIT License',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    ext_modules=extension,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
