from spm.__wrapper__ import Runtime


def spm_vb_neighbors(*args, **kwargs):
    """
      Create list of neighbors of voxels to be analysed  
        FORMAT vxyz = spm_vb_neighbors (xyz,vol)  
         
        xyz    - [Nvoxels x 3] list of voxel positions which are to be analysed  
        vol    - vol=1 for volumetric neighbors, vol=0 for within-slice neighbors   
                 (default vol=0)  
         
        vxyz   - [Nvoxels x 4] list of neighbouring voxels  
                 or [Nvoxels x 6] list of neighbouring voxels for vol=1  
         
                 vxyz(j,:)=[N1 N2 N3 0] means that there are only 3 neighbors  
                 of voxel j, and their numbers (ie. where they appear in the xyz  
                 list) are N1, N2 and N3  
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_vb_neighbors.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_vb_neighbors", *args, **kwargs)
