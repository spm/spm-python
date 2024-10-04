from spm.__wrap__ import _Runtime


def spm_mci_flow_sun(*args, **kwargs):
  """  Evaluate flow for Sundials routines  
    FORMAT [f, flag, new_data] = spm_mci_flow_sun (t, x, data)  
     
    t     time  
    x     state  
    data  .U inputs, .P parameters, .M model  
     
    f     flow, dx/dt  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/gradients/spm_mci_flow_sun.m)
  """

  return _Runtime.call("spm_mci_flow_sun", *args, **kwargs)
