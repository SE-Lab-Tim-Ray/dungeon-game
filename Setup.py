from distutils.core import setup

setup(
    name='JeffisLiar',
    packages = ['JeffisLiar'],
    version='1.7',
    license='MIT',
    description='JeffisLiar. Have fun with our game and help Jeff get out of the dungeon!',
    author='Binzhou Gu',
    author_email='bg548@bath.ac.uk',
    url='https://github.com/SE-Lab-Tim-Ray/dungeon-game/tree/installation',
    download_url='https://github.com/SE-Lab-Tim-Ray/dungeon-game/archive/V1.7.tar.gz',
    keywords=['DungeonGame', 'Joyful'],
    install_requires=[
        'pygame',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Games/Entertainment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
)