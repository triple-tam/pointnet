import sys, os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = BASE_DIR
sys.path.append(os.path.join(ROOT_DIR, 'utils'))

import numpy as np
import json


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

            groups = ['faceId', 'label']
            for g in groups:
                if g in path:
                    print np.array(f[g])

    return None



def explore_json(json_file):
    data=[]
    with open(json_file, "w") as f:
        json.dump(data, f)
    return data