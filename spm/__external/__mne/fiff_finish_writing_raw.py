from spm.__wrap__ import _Runtime


def fiff_finish_writing_raw(*args, **kwargs):
  """   
    function fiff_finish_writing_raw(fid)  
     
    fid        of an open raw data file  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_finish_writing_raw.m)
  """

  return _Runtime.call("fiff_finish_writing_raw", *args, **kwargs, nargout=0)
