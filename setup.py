from setuptools import setup
import os

packages = []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk('monte_carlo_gsa'):
    # Ignore dirnames that start with '.'
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)

setup(
    name='monte_carlo_gsa',
    version="0.0.1",
    packages=packages,
    author="Bernhard Steubing",
    author_email="b.r.p.steubing@cml.leidenuniv.nl",
    license="BSD 3-clause",
    url="https://github.com/bsteubing/lca-global-sensitivity-analysis",
    long_description=open('README.md').read(),
    description=('Implementing global sensitivity analysis functions for Life Cycle Assessment.'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics',
    ],
)