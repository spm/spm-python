from spm.__wrapper__ import Runtime


def spm_COVID_PV(*args, **kwargs):
    """
      FORMAT spm_COVID_PV(DCM,i,T)  
        remove ( > T) data from country ( = i)  
       --------------------------------------------------------------------------  
        i  - country index  
        T  - number of days to withhold  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_COVID_PV.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_COVID_PV", *args, **kwargs, nargout=0)
