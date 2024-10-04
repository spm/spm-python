from spm.__wrap__ import _Runtime


def mne_ex_cancel_noise(*args, **kwargs):
  """   
      Do projection and compensation as needed  
      Return the appropriate operators  
        
      [res,proj,comp] = mne_ex_cancel_noise(data,dest_comp)  
     
      res     - Data after noise cancellation  
      proj    - The projection operator applied  
      comp    - The compensator which brings uncompensated data to the  
                desired compensation grade (will be useful in forward  
                calculations)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_ex_cancel_noise.m)
  """

  return _Runtime.call("mne_ex_cancel_noise", *args, **kwargs)
