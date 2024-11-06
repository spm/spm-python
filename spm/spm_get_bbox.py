from spm.__wrapper__ import Runtime


def spm_get_bbox(*args, **kwargs):
    """
      Compute volume's bounding box, for full field of view or object bounds  
        FORMAT [BB,vx] = spm_get_bbox(V, thr)  
        V   - mapped image volume(s) (from spm_vol) or filename (empty for GUI)  
        thr - threshold, such that BB contains voxels with intensities > thr  
              or strings 'nz', 'nn', fv', for non-zero, non-NaN, or field of view  
              where 'fv' (the default) uses only the image's header information.  
         
        BB  - a [2 x 3] array of the min and max X, Y, and Z coordinates {mm},  
              i.e. BB = [minX minY minZ; maxX maxY maxZ].  
        vx  - a [1 x 3] vector of voxel dimensions {mm}.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_get_bbox.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_get_bbox", *args, **kwargs)
