import sys, os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = BASE_DIR
sys.path.append(os.path.join(ROOT_DIR, 'utils'))


from utils_by_tam import *
pointnet_root = '/usr/stud/tranthi/segmentation/03_repos/pointnet'


explore_h5(pointnet_root+'/sem_seg/indoor3d_sem_seg_hdf5_data/ply_data_all_0.h5')

print '\n'
# data_json = explore_json(pointnet_root+'/data/modelnet40_ply_hdf5_2048/ply_data_train_3_id2file.json')
# print type(data_json), len(data_json)
# print data_json[:10]

# import json
# from pprint import pprint
#
# with open(pointnet_root+'/data/modelnet40_ply_hdf5_2048/ply_data_train_0_id2file.json') as f:
#     data = json.load(f)
#
# pprint(data)