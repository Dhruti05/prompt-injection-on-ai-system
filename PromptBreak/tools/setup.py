from setuptools import setup, find_packages

setup(
    name='prompt-injection-tool',
    version='1.0',
    author='Dhruti',
    description='A simulation tool for studying prompt injection attacks on AI systems.',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'openai',
        'python-dotenv',
        'requests',
        'jinja2',
    ],
    entry_points={
        'console_scripts': [
            'prompt-injection-app = app:main'
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
