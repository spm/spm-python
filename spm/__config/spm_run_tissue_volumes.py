from spm._runtime import Runtime


def spm_run_tissue_volumes(*args, **kwargs):
    r"""
      SPM job execution function for Tissue Volumes  
         
        See also: spm_cfg_tissue_volumes, spm_summarise  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/config/spm_run_tissue_volumes.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_run_tissue_volumes", *args, **kwargs)
