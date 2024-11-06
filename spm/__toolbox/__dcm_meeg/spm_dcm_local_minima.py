from spm.__wrapper__ import Runtime


def spm_dcm_local_minima(*args, **kwargs):
    """
      Evaluate the free energy landscape around the posterior  
        FORMAT spm_dcm_local_minima(DCM)  
        DCM - (invert) model structure  
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_dcm_local_minima.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_local_minima", *args, **kwargs, nargout=0)
