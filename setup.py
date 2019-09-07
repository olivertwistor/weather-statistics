from setuptools import setup


setup(
    name="Weather Statistics",
    version="0.1.0",
    packages=[],
    entry_points={
        "console_scripts": [
            "weather_statistics = weather_statistics.__main__:main"
        ]
    }
)
