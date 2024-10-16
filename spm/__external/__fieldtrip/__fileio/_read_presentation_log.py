from spm.__wrapper__ import Runtime


def _read_presentation_log(*args, **kwargs):
  """  READ_PRESENTATION_LOG reads a NBS Presentation scenario log file and  
    represents it as a FieldTrip event structure.  
     
    See also FT_READ_EVENT  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_presentation_log.m)
  """

  return Runtime.call("read_presentation_log", *args, **kwargs)
