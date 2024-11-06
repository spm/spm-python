from spm.__wrapper__ import Runtime


def spm_vb_contrasts(*args, **kwargs):
    """
      Compute and write posterior standard deviation image of given contrast  
        FORMAT SPM = spm_vb_contrasts(SPM,XYZ,xCon,ic)  
         
        SPM   - SPM data structure  
        XYZ   - voxel list  
        xCon  - contrast info  
        ic    - contrast number  
         
        Get approximate posterior covariance for given contrast ic using   
        Taylor-series approximation  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_vb_contrasts.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_vb_contrasts", *args, **kwargs)
