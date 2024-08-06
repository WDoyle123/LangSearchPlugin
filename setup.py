from setuptools import setup, find_packages

setup(
    name='lang_search_plugin',
    version='0.1',
    description='A custom language search plugin for MkDocs',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='William Doyle',
    author_email='william.e.doyle.contact@gmail.com',
    url='https://github.com/wdoyle123/LangSearchPlugin',  
    license='MIT',
    packages=find_packages(),
    install_requires=['mkdocs'],
    entry_points={
        'mkdocs.plugins': [
            'lang_search_plugin = lang_search_plugin:LangSearchPlugin',
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)

