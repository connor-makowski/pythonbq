from distutils.core import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
  name = 'pythonbq',
  packages = ['pythonbq'],
  version = '1.0.0',
  license='MIT',
  description = 'Python wrapper for easy use of big query',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Connor Makowski',
  author_email = 'connor.m.makowski@gmail.com',
  url = 'https://github.com/connor-makowski/pythonbq',
  download_url = 'https://github.com/connor-makowski/pythonbq/dist/pythonbq-1.0.0.tar.gz',
  keywords = ['bigquery', 'big', 'query', 'pythonbq'],
  install_requires=[
          'google-cloud-bigquery==3.6.0',
          'type_enforced>=0.0.15'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
  ],
)
