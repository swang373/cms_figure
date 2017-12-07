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
    packages=find_packages(),
    description='Styling and labels for CMS figures produced using ROOT',
    author='Sean-Jiun Wang',
    author_email='sean.jiun.wang@gmail.com',
    maintainer='Sean-Jiun Wang',
    maintainer_email='sean.jiun.wang@gmail.com',
    url='https://github.com/swang373/cms_figure',
    download_url='https://github.com/swang373/cms_figure/tarball/{0}'.format(version),
    license='MIT',
    python_requires='>=2.7, <3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
)

