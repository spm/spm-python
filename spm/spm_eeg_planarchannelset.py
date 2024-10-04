from spm.__wrap__ import _Runtime


def spm_eeg_planarchannelset(*args, **kwargs):
  """  Define the planar gradiometer channel combinations  
    FORMAT planar = spm_eeg_planarchannelset(data)  
     
    The output cell array contains the horizontal label, vertical label and  
    the label after combining the two.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_planarchannelset.m)
  """

  return _Runtime.call("spm_eeg_planarchannelset", *args, **kwargs)
