from spm.__wrapper__ import Runtime


def spm_mci_switch_prep(*args, **kwargs):
  """  Prepare quantities for computing log prior in SVD-reduced space  
    FORMAT [M] = spm_mci_switch_prep (M)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_switch_prep.m)
  """

  return Runtime.call("spm_mci_switch_prep", *args, **kwargs)
