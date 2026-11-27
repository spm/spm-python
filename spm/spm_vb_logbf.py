from spm._runtime import Runtime


def spm_vb_logbf(*args, **kwargs):
    r"""
      Compute and write log Bayes factor image  
        FORMAT [xCon,SPM] = spm_vb_logbf(SPM,XYZ,xCon,ic)  
         
        SPM    - SPM data structure  
        XYZ    - voxel list  
        xCon   - contrast info  
        ic     - contrast number  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_vb_logbf.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_vb_logbf", *args, **kwargs)
