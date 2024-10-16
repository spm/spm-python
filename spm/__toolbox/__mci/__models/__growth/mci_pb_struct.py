from spm.__wrapper__ import Runtime


def mci_pb_struct(*args, **kwargs):
  """  Preece-Baines model structure  
    FORMAT [M,U] = mci_pb_struct (Nobs)  
     
    Nobs      Number of observations  
     
    M         Model structure  
    U         Input structure  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/growth/mci_pb_struct.m)
  """

  return Runtime.call("mci_pb_struct", *args, **kwargs)
