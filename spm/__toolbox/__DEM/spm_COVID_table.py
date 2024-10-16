from spm.__wrapper__ import Runtime


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

  return Runtime.call("spm_COVID_table", *args, **kwargs)
