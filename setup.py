from setuptools import setup


setup(
    name="Weather Statistics",
    version="0.1.0",
    packages=[],
    entry_points={
        "console_scripts": [
            "weatherstats = weatherstats.__main__:main"
        ]
    }
)
