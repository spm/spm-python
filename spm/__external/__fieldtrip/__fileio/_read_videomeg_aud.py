from spm.__wrapper__ import Runtime


def _read_videomeg_aud(*args, **kwargs):
  """  READ_VIDEOMEG_AUD  
     
    Use as  
      hdr = read_videomeg_aud(filename)  
    or  
      dat = read_videomeg_aud(filename, hdr, begsample, endsample)  
     
    See also READ_VIDEOMEG_VID, LOAD_AUDIO0123, LOAD_VIDEO123  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_videomeg_aud.m)
  """

  return Runtime.call("read_videomeg_aud", *args, **kwargs)
