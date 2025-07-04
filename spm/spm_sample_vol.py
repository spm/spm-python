from spm._runtime import Runtime


def spm_sample_vol(*args, **kwargs):
    """
      Return voxel values from an image volume - a compiled routine  
        FORMAT X = spm_sample_vol(V,x,y,z,hold)  
        V        -  spm_vol structure  
        x        -  matrix of x coordinates {voxels}  
        y        -  matrix of y coordinates {voxels}  
        z        -  matrix of z coordinates {voxels}  
        hold     -  interpolation method for the resampling:  
                     0         : Zero-order hold (nearest neighbour)  
                     1         : First-order hold (trilinear interpolation)  
                     2->127    : Higher order Lagrange (polynomial) interpolation  
                                 using different holds (second-order upwards)  
                     -127 - -1 : Different orders of sinc interpolation  
          
        X        -  output image  
         
        FORMAT [X,dX,dY,dZ] = spm_sample_vol(V,x,y,z,hold)  
        Similar to above, except that the derivatives in the three orthogonal  
        directions are also returned.  
       __________________________________________________________________________  
         
        spm_sample_vol returns the voxel values from an image volume indicated  
        by V at coordinates x,y,z.  Values from coordinates outside the image  
        are set to zero. x, y and z must be matrices of the same dimensions.  
         
        See also: spm_vol.m, spm_slice_vol.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_sample_vol.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_sample_vol", *args, **kwargs)
