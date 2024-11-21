from spm.__wrapper__ import Runtime


def spm_dcm_csd_source_optimise(*args, **kwargs):
    """
      Stochastic optimisation of single source neural mass model  
        FORMAT [PE] = spm_dcm_csd_source_optimise  
         
        Edit the set up variable in the main body of this routine to specify   
        desired frequency responses (in selected populations)  
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_dcm_csd_source_optimise.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_csd_source_optimise", *args, **kwargs)
