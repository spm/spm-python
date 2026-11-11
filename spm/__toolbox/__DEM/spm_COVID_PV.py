from spm._runtime import Runtime


def spm_COVID_PV(*args, **kwargs):
    r"""
      FORMAT spm_COVID_PV(DCM,i,T)  
        remove ( > T) data from country ( = i)  
       --------------------------------------------------------------------------  
        i  - country index  
        T  - number of days to withhold  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_COVID_PV.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_COVID_PV", *args, **kwargs, nargout=0)
