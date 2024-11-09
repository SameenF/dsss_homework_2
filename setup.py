from setuptools import setup, find_packages

setup(
    name="dsss_homework_2",
    version="1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:math_quiz',
        ],
    },
    test_suite="math_quiz/tests_math_quiz.py",
    author="Yiting Feng",
    author_email="fengyiting_hear@163.com",
    description="A simple math quiz game.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/SameenF/dsss_homework_2",
    license="Apache License 2.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
