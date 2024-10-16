from spm.__wrapper__ import Runtime


def mne_make_compensator(*args, **kwargs):
  """   
    [comp] = mne_make_compensator(info,from,to,exclude_comp_chs)  
     
    info              - measurement info as returned by the fif reading routines  
    from              - compensation in the input data  
    to                - desired compensation in the output  
    exclude_comp_chs  - exclude compensation channels from the output (optional)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_make_compensator.m)
  """

  return Runtime.call("mne_make_compensator", *args, **kwargs)
