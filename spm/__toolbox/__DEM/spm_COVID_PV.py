from spm.__wrapper__ import Runtime


def spm_COVID_PV(*args, **kwargs):
  """  FORMAT spm_COVID_PV(DCM,i,T)  
    remove ( > T) data from country ( = i)  
   --------------------------------------------------------------------------  
    i  - country index  
    T  - number of days to withhold  
   __________________________________________________________________________  
    Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_COVID_PV.m)
  """

  return Runtime.call("spm_COVID_PV", *args, **kwargs, nargout=0)
