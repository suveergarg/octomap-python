import numpy as np 
import octomap

import numpy as np
import time
import octomap

class VoxelMap():

    def __init__(self, map_size = 1, map_res = 1e-2 * 5):
        self.map_size = map_size #in meter

        self.map_res = map_res #in meter
        self.octmap = octomap.SemanticOcTree(self.map_res)

        #For filtering PC till this is made configurable
        self.x_range_max = 1  #In meters
        self.x_range_min = 0
        self.y_range_max = 0.5
        self.y_range_min = -0.5
        self.z_range_max = 1
        self.z_range_min = 0.05 

    def points_in_range(self, pc):
        idxx = np.logical_and(pc[0,:]<self.x_range_max, pc[0, :]>self.x_range_min)
        idxy = np.logical_and(pc[1,:]<self.y_range_max, pc[1, :]>self.y_range_min)
        idxz = np.logical_and(pc[2,:]<self.z_range_max, pc[2, :]>self.z_range_min)

        idx = np.logical_and(np.logical_and(idxx, idxy), idxz)

        return pc[:, idx]

    def update_vmap(self, np_points, camera_origin, est_category, confidence, id):
        '''
            Updates internal state of voxel map 
            input: point cloud as a n*dims array
        '''
        start_time = time.time()
        #Just in case before we filter points early in the pipeline
        np_points_in_range = self.points_in_range(np_points.T).T #in range points
        
        pc_np_xyz = np_points_in_range[:, :3]
        
        #TODO: check params again
        self.octmap.insertPointCloudAndSemantics(
            pointcloud=pc_np_xyz.astype(np.double),
            origin=camera_origin,
            id = id,
            est_category = est_category,
            confidence = confidence,
            maxrange=2,
            lazy_eval = False,
            discretize = False
        )
        self.octmap.updateInnerOccupancy()

        print("time to update map: ", time.time()-start_time)


vmap = VoxelMap()
pc = np.random.rand(1000,3)
vmap.update_vmap(pc, np.array([0.0, 0.0, 0.0]), 1, 0.5, 3)
pc = np.random.rand(1000,3)
vmap.update_vmap(pc, np.array([0.0, 0.0, 0.0]), 2, 0.5, 3)

occupied, empty = vmap.octmap.extractPointCloud()
print(occupied.shape)
print(empty.shape)

