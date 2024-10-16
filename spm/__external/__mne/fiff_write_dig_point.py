from spm.__wrapper__ import Runtime


def fiff_write_dig_point(*args, **kwargs):
  """   
    fiff_write_dig_point(fid,dig)  
      
    Writes a digitizer data point into a fif file  
     
        fid           An open fif file descriptor  
        dig           The point to write  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_write_dig_point.m)
  """

  return Runtime.call("fiff_write_dig_point", *args, **kwargs, nargout=0)
