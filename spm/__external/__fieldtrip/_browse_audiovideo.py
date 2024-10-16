from spm.__wrapper__ import Runtime


def _browse_audiovideo(*args, **kwargs):
  """  BROWSE_AUDIOVIDEO reads and vizualizes the audio and/or video data  
    corresponding to the EEG/MEG data segment that is passed into this  
    function.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/browse_audiovideo.m)
  """

  return Runtime.call("browse_audiovideo", *args, **kwargs, nargout=0)
