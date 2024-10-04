from spm.__wrap__ import _Runtime


def mci_nmm_struct(*args, **kwargs):
  """  Set up two region NMM   
    FORMAT [M,U] = mci_nmm_struct (back,sd,Np)  
     
    back      1 to include backward connection (default)  
    sd        Observation noise SD (default 0.01)  
    Np        number of params (2,6 or 21)  
     
    M         Model structure  
    U         Inputs  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/nmm/mci_nmm_struct.m)
  """

  return _Runtime.call("mci_nmm_struct", *args, **kwargs)
