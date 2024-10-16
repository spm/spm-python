from spm.__wrapper__ import Runtime


def _read_spmeeg_header(*args, **kwargs):
  """  read_spmeeg_header() - import SPM5 and SPM8 meeg datasets  
     
    Usage:  
      >> header = read_spmeeg_header(filename);  
     
    Inputs:  
      filename - [string] file name  
     
    Outputs:  
      header   - FILEIO toolbox type structure  
    _______________________________________________________________________  
    Copyright (C) 2008 Wellcome Trust Centre for Neuroimaging  
    Vladimir Litvak  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_spmeeg_header.m)
  """

  return Runtime.call("read_spmeeg_header", *args, **kwargs)
