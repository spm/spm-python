from spm.__wrapper__ import Runtime


def _interp_ungridded(*args, **kwargs):
    """
      INTERP_UNGRIDDED computes an interpolation matrix for two clouds of 3-D points  
         
        To get the interpolated data, use as  
          [valto] = interp_ungridded(pos_from, pos_to, 'data', valfrom, ...)  
        or to get the interpolation matrix itself, use as  
          [interpmat, distmat] = interp_ungridded(pos_from, pos_to, ...)  
        where  
          pos_from  Nx3 matrix with the vertex positions  
          pos_to    Mx3 matrix with the vertex positions onto which the data should be interpolated  
         
        Optional arguments are specified in key-value pairs and can be  
           data         = NxK matrix with functional data  
           distmat      = NxM matrix with precomputed distances  
           projmethod   = 'nearest', 'sphere_avg', 'sphere_weighteddistance', 'smudge'  
           triout       = triangulation for the second set of vertices  
           sphereradius = scalar  
           power        = scalar, power parameter as in the Inverse Distance Weighting function proposed by Shepard (default = 1).  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/interp_ungridded.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("interp_ungridded", *args, **kwargs)
