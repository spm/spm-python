from spm.__wrap__ import _Runtime


def dcm_fit_finger(*args, **kwargs):
  """  Fit DCM model to finger data  
    FORMAT [DCM] = dcm_fit_finger(yy,M,U,m)  
     
    yy     -  yy{n} for nth trial data  
    M      -  model structure  
    U      -  input structure  
    m      -  PIF order  
     
    DCM    -  o/p data structure  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/man/example_scripts/dcm_fit_finger.m)
  """

  return _Runtime.call("dcm_fit_finger", *args, **kwargs)
