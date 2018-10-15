from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='pyaudioclassification',
      version='0.1',
      description='Dead simple audio classification',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Audio Processing :: Audio Classification',
      ],
      keywords='simple audio classification',
      url='http://github.com/storborg/funniest',
      author='98mprice',
      author_email='98mprice@gmail.com',
      license='MIT',
      packages=['pyaudioclassification'],
      install_requires=[
          'numpy',
          'librosa',
          'soundfile',
          'tqdm',
          'keras'
      ],
      scripts=['bin/feature_extraction'],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False)
