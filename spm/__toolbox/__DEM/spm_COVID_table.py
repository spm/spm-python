from spm.__wrap__ import _Runtime


def spm_COVID_table(*args, **kwargs):
  """  FORMAT Tab = spm_COVID_table(Ep,Cp,M)  
    FORMAT Tab = spm_COVID_table(DCM)  
    Ep  - conditional expectations  
    Cp  - conditional covariances  
    M   - model  
     
    Tab - table of conditional estimators  
   __________________________________________________________________________  
    Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_COVID_table.m)
  """

  return _Runtime.call("spm_COVID_table", *args, **kwargs)
