from spm.__wrapper__ import Runtime


def _interp_gridded(*args, **kwargs):
    """
      INTERP_GRIDDED computes a matrix that interpolates values that were  
        observed on positions in a regular 3-D grid onto positions that are  
        unstructured, e.g. the vertices of a cortical sheet.  
         
        Use as  
          [val]                = interp_gridded(transform, val, pos, ...) or  
          [interpmat, distmat] = interp_gridded(transform, val, pos, ...)  
        where  
          transform  homogenous coordinate transformation matrix for the volume  
          val        3-D matrix with the values in the volume  
          pos        Mx3 matrix with the vertex positions onto which the data should  
                     be interpolated  
         
        Optional arguments are specified in key-value pairs and can be  
           projmethod   = 'nearest', 'sphere_avg', 'sphere_weighteddistance'  
           sphereradius = number  
           distmat      = NxM matrix with precomputed distances  
           inside       = indices for inside voxels (or logical array)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/interp_gridded.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("interp_gridded", *args, **kwargs)
