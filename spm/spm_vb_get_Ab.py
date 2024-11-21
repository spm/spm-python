from spm.__wrapper__ import Runtime


def spm_vb_get_Ab(*args, **kwargs):
    """
      Get A and b quantities - average prediction errors from AR model  
        FORMAT [voxel] = spm_vb_get_Ab(Y,slice)  
          
        Y      - [T x N] time series  
        slice  - data structure (see spm_vb_glmar)  
          
        voxel(n).A    
        voxel(n).b  
         
        The above quantities are estimated using pre-computed  
        cross-covariance matrices  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_vb_get_Ab.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_vb_get_Ab", *args, **kwargs)
