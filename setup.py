import setuptools
from pathlib import Path

setuptools.setup(
    name='min-dalle',
    description = 'min(DALL·E)',
    long_description=(Path(__file__).parent / "README").read_text(),
    version='0.2.6',
    author='Brett Kuprel',
    author_email='brkuprel@gmail.com',
    url='https://github.com/kuprel/min-dalle',
    packages=[
        'min_dalle', 
        'min_dalle.models'
    ],
    license='MIT',
    install_requires=[
        'torch>=1.10.0'
    ],
    keywords = [
        'artificial intelligence',
        'deep learning',
        'text-to-image',
        'pytorch'
    ]
)