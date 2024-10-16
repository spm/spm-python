from spm.__wrapper__ import Runtime


def _read_bti_m4d(*args, **kwargs):
  """  READ_BTI_M4D  
     
    Use as  
      msi = read_bti_m4d(filename)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_bti_m4d.m)
  """

  return Runtime.call("read_bti_m4d", *args, **kwargs)
