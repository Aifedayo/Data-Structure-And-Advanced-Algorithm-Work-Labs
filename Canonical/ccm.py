from contextlib import contextmanager

@contextmanager
def custom_manager(resource):
    print('Resource acquired')
    yield resource
    print('Resource released')


with custom_manager('Example Resource') as res:
    print(f'Using {res}')