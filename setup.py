import ast
import re

from setuptools import setup, find_packages


try:
    import ROOT
except ImportError:
    raise ImportError('Unable to import ROOT. Please check that ROOT and its Python bindings are installed.')
ROOT.PyConfig.IgnoreCommandLineOptions = True


VERSION_RE = re.compile(r'__version__\s+=\s+(.*)')


with open('cms_figure/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(VERSION_RE.search(f.read().decode('utf-8')).group(1)))


setup(
    name='cms_figure',
    version=version,
    description='Styling and labels for CMS figures produced using ROOT',
    url='https://github.com/swang373/cms_figure',
    download_url='https://github.com/swang373/vhbbtools/tarball/{0}'.format(version),
    author='Sean-Jiun Wang',
    author_email='sean.jiun.wang@gmail.com',
    license='MIT',
    packages=find_packages(),
    python_requires='>=2.7, <3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Physics',
    ],
)

