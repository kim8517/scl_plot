from setuptools import setup, find_packages

setup(
    name='scl_plot',
    version='0.1',
    packages=find_packages(),
    install_requires=['matplotlib'],
    entry_points={
        'console_scripts': [
            # 'script_name = my_package.myscript:main_function',
        ],
    },
    include_package_data=True,
    description='Python matplotlib settings for SNUCLUES',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='TAEWAN KIM',
    author_email='ktwa8517@gmail.com',
    url='https://github.com/kim8517/scl_plot.git',  # Update with your package URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.',
)