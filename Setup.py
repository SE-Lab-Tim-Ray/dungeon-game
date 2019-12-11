from distutils.core import setup

setup(
    name='JeffisLiar',
    packages = ['JeffisLiar'],
    version='1.9',
    license='MIT',
    description='JeffisLiar. Have fun with our game and help Jeff get out of the dungeon!',
    author='Binzhou Gu',
    author_email='bg548@bath.ac.uk',
    url='https://github.com/SE-Lab-Tim-Ray/dungeon-game/tree/installation',
    download_url='https://github.com/SE-Lab-Tim-Ray/dungeon-game/archive/V1.9.tar.gz',
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
        'Programming Language :: Python :: 3.8',
    ],
    include_package_data=True,
    data_files=[
        ('data', ['JeffisLiar/data/1_char.png', 'JeffisLiar/data/1_lose.png', 'JeffisLiar/data/1_maze.png',
                  'JeffisLiar/data/1_maze.txt', 'JeffisLiar/data/1_win.png', 'JeffisLiar/data/rat.png'])
    ],
)