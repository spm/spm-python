from spm.__wrapper__ import Runtime


def spm_DEM_qH(*args, **kwargs):
  """  Report on conditional estimates of hyperparameters  
    FORMAT spm_DEM_qH(qH,pH)  
     
    qH.h    - conditional estimate of log-precision (causes)  
    qH.g    - conditional of log-precision (state)  
    qH.V    - conditional variance (causes)  
    qH.W    - conditional (states)  
     
    qH.p    - time-dependent estimates from Laplace scheme  
    qH.c    - time-dependent covariances  
     
    pH      - option true log-precisions  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_DEM_qH.m)
  """

  return Runtime.call("spm_DEM_qH", *args, **kwargs, nargout=0)
