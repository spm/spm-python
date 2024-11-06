from spm.__wrapper__ import Runtime


def spm_TVdenoise(*args, **kwargs):
    """
      Joint total variation denoising of 3D volumes  
        FORMAT y = spm_TVdenoise(x, vox, lambdap, lambdal, nit, y)  
        x        - a 3D or 4D array/gpuArray of floating point data  
        vox      - voxel sizes [1 1 1]  
        lambdap  - regularisation of each channel (along 4th dimension) [1]  
        lambdal  - reciprocals of variances (along 4th dimension) [1]  
        nit      - number of iterations [100]  
        y        - starting estimates [x]  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Spatial/spm_TVdenoise.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_TVdenoise", *args, **kwargs)
