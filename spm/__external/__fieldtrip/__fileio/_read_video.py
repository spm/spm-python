from spm.__wrap__ import _Runtime


def _read_video(*args, **kwargs):
  """  READ_VIDEO  
     
    Use as  
      hdr = read_video(filename)  
    or  
      dat = read_video(filename, hdr, begsample, endsample)  
     
    See also READ_VIDEOMEG_VID, LOAD_VIDEO123  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_video.m)
  """

  return _Runtime.call("read_video", *args, **kwargs)
