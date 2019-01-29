import sys, os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = BASE_DIR
sys.path.append(os.path.join(ROOT_DIR, 'utils'))

import numpy as np
import json
import matplotlib.pyplot as plt
from open3d.open3d.geometry import read_point_cloud


def explore_h5(hdf_file):

    """Traverse all datasets across all groups in HDF5 file."""

    import h5py

    def h5py_dataset_iterator(g, prefix=''):
        for key in g.keys():
            item = g[key]
            path = '{}/{}'.format(prefix, key)
            if isinstance(item, h5py.Dataset): # test for dataset
                yield (path, item)
            elif isinstance(item, h5py.Group): # test for group (go down)
                for h in h5py_dataset_iterator(item, path):
                    yield h

    with h5py.File(hdf_file, 'r') as f:
        for (path, dset) in h5py_dataset_iterator(f):
            print(path, dset)

            groups = ['data', 'faceId', 'label', 'try']
            for g in groups:
                if g in path:
                    print np.array(f[g])

    return None



# bad, need to fix. it clears all data in .json file
def explore_json(json_file):
    data=[]
    with open(json_file, "w") as f:
        json.dump(data, f)
    return data


def parse_log_file(log_file, items):
    # parse and plot
    # values = list of items
    file = open(log_file, 'r')
    values = {}
    for i in items:
        values[i] = []

    for l in file:
        precolon = l.split(':')[0]
        postcolon = l.split(':')[-1]
        if precolon in items:
            values[precolon].append(float(postcolon))

    plt.figure()
    for i,v in values.items():
        plt.plot(v, label=i)
        for a,b in zip(range(len(v)), v):
            if a%5==0:
                plt.text(a,b,str(b)[:4])
    plt.title(log_file.split('/')[-1])
    plt.legend()

    plt.show()

    return values



def sum_dims(directory, file_type):

    shape_total = np.zeros((1,2))
    for file in os.listdir(directory):
        if file.endswith('.'+file_type):
            #shape = np.asarray(np.asarray(np.load(directory + '/' + file)).shape())
            shape = np.asarray(np.asarray(np.load(directory + '/' + file)).shape)
            print(shape)
            shape_total += shape


            data = np.load(directory + '/' + file)
            data = np.asarray(data)
            shape = data.shape
            shape = np.asarray(shape)
            print(shape)
            shape_total += shape

    print('shape_total', shape_total)
    return shape_total


def ply_to_npy(in_ply_file, out_npy_file):
    # gives fake label
    ply = read_point_cloud(in_ply_file)
    n = np.asarray(ply.points).shape[0]
    npy = np.zeros((n, 7))
    npy[:,:3] = np.asarray(ply.points)
    npy[:,3:6] = np.asarray(ply.colors)

    np.save(out_npy_file, npy)