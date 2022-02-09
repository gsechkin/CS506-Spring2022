import pandas as pd

def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    temp = pd.read_csv(csv_file_path, header=None)
    return [list(row) for row in temp.values]
    # raise NotImplementedError()
