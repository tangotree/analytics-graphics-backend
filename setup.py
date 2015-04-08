from setuptools import setup

if __name__ == '__main__':
    setup(
        name          = 'api',
        packages      = ['app'],
        package_data  = {
            'data'       : ['data'],
        },
        zip_safe      = False,
    )
