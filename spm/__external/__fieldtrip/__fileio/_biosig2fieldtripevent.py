from spm.__wrap__ import _Runtime


def _biosig2fieldtripevent(*args, **kwargs):
  """  BIOSIG2FIELDTRIPEVENT converts event information from a biosig hdr into  
    fieldtrip events  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/biosig2fieldtripevent.m)
  """

  return _Runtime.call("biosig2fieldtripevent", *args, **kwargs)
