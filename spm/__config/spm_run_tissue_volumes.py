from spm.__wrapper__ import Runtime


def spm_run_tissue_volumes(*args, **kwargs):
    """
      SPM job execution function for Tissue Volumes  
         
        See also: spm_cfg_tissue_volumes, spm_summarise  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_run_tissue_volumes.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_run_tissue_volumes", *args, **kwargs)
