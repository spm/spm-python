from spm._runtime import Runtime


def spm_smooth_extrap(*args, **kwargs):
    r"""
      Fast convolution Gaussian smoothing in 3D plus extrapolation to missing data  
        FORMAT v = spm_smooth_extrap(image, mask, k, Niter)  
        Inputs:  
          image: 3D image to be smoothed    
          mask: 3D binary mask defining voxels with valid data  
          k: Scalar smoothing kernel in image domain specified in voxels  
          Niter: number of iteration steps used for extrapolation  
        Output:  
          image: Smoothed 3D image  
         
          Barbara Dymerska, Oliver Josephs  
          Copyright (C) 2025 Department of Imaging Neuroscience, UCL  
       ==========================================================================  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/Spatial/spm_smooth_extrap.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_smooth_extrap", *args, **kwargs)
