from spm.__wrap__ import _Runtime


def mci_compare_jacobians(*args, **kwargs):
  """  Compare user supplied and finite difference methods  
    FORMAT [Fx,Fp,FxFD,FpFD] = mci_compare_jacobians (model)  
     
    model     'phase'  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/demo-gradients/mci_compare_jacobians.m)
  """

  return _Runtime.call("mci_compare_jacobians", *args, **kwargs)
