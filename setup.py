from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='audioclassification',
      version='0.1.9',
      description='A Dead simple audio classification',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.0'
      ],
      keywords='simple audio classification',
      url='https://github.com/puneetkakkar/audio-classification',
      author='puneetkakkar',
      author_email='puneetkakkar91@gmail.com',
      license='MIT',
      packages=['audioclassification'],
      install_requires=[
          'numpy',
          'librosa',
          'soundfile',
          'tqdm',
          'keras',
	  'matplotlib'
      ],
      scripts=['bin/feature_extraction'],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False)
