from spm.__wrap__ import _Runtime


def mci_pb_gen(*args, **kwargs):
  """  Preece-Baines growth model  
    FORMAT [y] = mci_pb_gen (P,M,U)  
     
    P         parameters  
    M         model  
    U         inputs  
     
    y         time series  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/growth/mci_pb_gen.m)
  """

  return _Runtime.call("mci_pb_gen", *args, **kwargs)
