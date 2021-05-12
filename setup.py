from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0'
DESCRIPTION = 'A powerful os operating system for python with exclusive functions'

# Setting up
setup(
    name="vidstream",
    version=VERSION,
    author="Aarav Shreshth",
    author_email="aaravshreshth1503@gmail.com",
    description=DESCRIPTION,
    long_description="A powerful os",
    packages=find_packages(),
    install_requires=['opencv-python', 'pyautogui'],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
