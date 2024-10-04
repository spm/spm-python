from spm.__wrap__ import _Runtime


def _read_biosig_data(*args, **kwargs):
  """  READ_BIOSIG_DATA reads data from EEG file using the BIOSIG  
    toolbox and returns it in the FCDC framework standard format  
     
    Use as  
     [dat] = read_biosig_data(filename, hdr, begsample, endsample, chanindx)  
    where the header has to be read before with READ_BIOSIG_HEADER.  
     
    The following data formats are supported: EDF, BKR, CNT, BDF, GDF  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_biosig_data.m)
  """

  return _Runtime.call("read_biosig_data", *args, **kwargs)
