from spm.__wrap__ import _Runtime


def spm_mci_adjoint_int(*args, **kwargs):
  """  Integrate adjoint equation  
    FORMAT [lambda] = spm_mci_adjoint_int (U,P,M,V,djdx,tol)  
     
    U         Inputs  
    P         Parameters  
    M         Model structure  
    V         states  
    djdx      derivative of log likelihood wrt states  
    tol       tolerances  
     
    lambda    adjoint parameters, at times M.t  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/gradients/spm_mci_adjoint_int.m)
  """

  return _Runtime.call("spm_mci_adjoint_int", *args, **kwargs)
