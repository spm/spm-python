from spm._runtime import Runtime


def spm_vb_contrasts(*args, **kwargs):
    r"""
      Compute and write posterior standard deviation image of given contrast  
        FORMAT SPM = spm_vb_contrasts(SPM,XYZ,xCon,ic)  
         
        SPM   - SPM data structure  
        XYZ   - voxel list  
        xCon  - contrast info  
        ic    - contrast number  
         
        Get approximate posterior covariance for given contrast ic using   
        Taylor-series approximation  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_vb_contrasts.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_vb_contrasts", *args, **kwargs)
