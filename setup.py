from distutils.core import setup

setup(
    name="crop_image",  # How you named your package folder (MyLib)
    packages=["crop_image"],  # Chose the same as "name"
    version="0.1",  # Start with a small number and increase it with every change you make
    license="MIT",  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description="Crop images based on a reference image or providing dimensions",  # Give a short description about your library
    author="Giulia Martini",  # Type in your name
    author_email="martini.giulia94@gmail.com",  # Type in your E-Mail
    url="https://github.com/martinig94",  # Provide either the link to your github or to your website
    download_url="https://github.com/martinig94/crop_image/archive/refs/tags/v0.1-alpha.tar.gz",
    keywords=["crop", "picture", "image"],  # Keywords that define your package best
    install_requires=["Pillow"],
    classifiers=[
        "Development Status :: 3 - Alpha",  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Intended Audience :: Developers",  # Define that your audience are developers
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",  # Again, pick a license
        "Programming Language :: Python :: 3.8",
    ],
)
