from spm.__wrapper__ import Runtime


def _plx_orig_header(*args, **kwargs):
  """  PLX_ORIG_HEADER Extracts the header informations of plx files using the  
    Plexon Offline SDK, which is available from  
    http://www.plexon.com/assets/downloads/sdk/ReadingPLXandDDTfilesinMatlab-mexw.zip  
     
    Use as  
      [orig] = plx_orig_header(filename)  
     
    Copyright (C) 2012 by Thomas Hartmann  
     
    This code can be redistributed under the terms of the GPL version 3 or  
    newer.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/plx_orig_header.m)
  """

  return Runtime.call("plx_orig_header", *args, **kwargs)
