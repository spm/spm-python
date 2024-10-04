from spm.__wrap__ import _Runtime


def spm_mci_like_ind(*args, **kwargs):
  """  Compute likelihood wrt selected time points  
    FORMAT [L,e] = spm_mci_like_ind (P,R,M,U,Y)  
     
    P         Flow parameters  
    R         Initial state parameters  
    M         Model structure  
    U         Inputs  [Nin x N]  
    Y         data  
          
    L         Log likelihood  
    e         Prediction errors  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_like_ind.m)
  """

  return _Runtime.call("spm_mci_like_ind", *args, **kwargs)
