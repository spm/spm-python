from spm.__wrapper__ import Runtime


def _read_biosig_header(*args, **kwargs):
  """  READ_BIOSIG_HEADER reads header from EEG file using the BIOSIG  
    toolbox and returns it in the FCDC framework standard format  
     
    Use as  
     [hdr] = read_biosig_header(filename)  
     
    The following data formats are supported: EDF, BKR, CNT, BDF, GDF,  
    see for full documentation http://biosig.sourceforge.net/  
     
    See also READ_BIOSIG_DATA  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_biosig_header.m)
  """

  return Runtime.call("read_biosig_header", *args, **kwargs)
