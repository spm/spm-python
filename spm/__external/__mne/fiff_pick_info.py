from spm.__wrap__ import _Runtime


def fiff_pick_info(*args, **kwargs):
  """   
    [res] = fiff_pick_info(info,sel)  
     
    Pick desired channels from measurement info  
     
    res       - Info modified according to sel  
    info      - The original data  
    sel       - List of channels to select  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_pick_info.m)
  """

  return _Runtime.call("fiff_pick_info", *args, **kwargs)
