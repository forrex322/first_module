import csv
from contextlib import contextmanager


class ContextManagerAppender(object):

    def __init__(self, file_name):
        if not file_name.endswith('.csv'):
            print('File must be .csv')
            raise Exception('File must be .csv')
        self.file_name = file_name

    def __enter__(self):
        self.file = open(self.file_name, 'a', newline='')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()


@contextmanager
def append_file(file_name):
    if not file_name.endswith('.csv'):
        print('File must be .csv')
        raise Exception('File must be .csv')

    file = open(file_name, mode='a', newline='')
    try:
        yield file
    finally:
        file.close()


filename = 'test.csv'

data3 = [[f'Bob; {22}'], [f'Bib; {20}'], [f'Bab; {23}']]
with ContextManagerAppender(filename) as xfile:
    csvappender = csv.writer(xfile)
    csvappender.writerows(data3)

data4 = [[f'Foo; {22}'], [f'Baz; {20}'], [f'Bar; {23}']]
with append_file(filename) as file:
    csvappender = csv.writer(file)
    csvappender.writerows(data4)
