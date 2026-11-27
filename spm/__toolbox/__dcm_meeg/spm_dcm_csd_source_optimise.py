from spm._runtime import Runtime


def spm_dcm_csd_source_optimise(*args, **kwargs):
    r"""
      Stochastic optimisation of single source neural mass model  
        FORMAT [PE] = spm_dcm_csd_source_optimise  
         
        Edit the set up variable in the main body of this routine to specify   
        desired frequency responses (in selected populations)  
         
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/dcm_meeg/spm_dcm_csd_source_optimise.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dcm_csd_source_optimise", *args, **kwargs)
