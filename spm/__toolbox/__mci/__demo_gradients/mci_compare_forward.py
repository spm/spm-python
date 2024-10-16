from spm.__wrapper__ import Runtime


def mci_compare_forward(*args, **kwargs):
  """  Compare integration methods   
    FORMAT [els_sun,els_ode,els_spm] = mci_compare_forward (model)  
     
    model     'phase', 'nmm-r2p2'  
     
    Run integration 9 times - compare speed and accuracy  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/demo-gradients/mci_compare_forward.m)
  """

  return Runtime.call("mci_compare_forward", *args, **kwargs)
