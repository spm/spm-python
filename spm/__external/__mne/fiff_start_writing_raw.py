from spm.__wrapper__ import Runtime


def fiff_start_writing_raw(*args, **kwargs):
  """   
    function [fid,cals] = fiff_start_writing_raw(name,info,sel)  
     
    name       filename  
    info       The measurement info block of the source file  
    sel        Which channels will be included in the output file (optional)  
    precision  Numeric precision with which the data will be written  
               (optional). Default 'single', can also be 'double'  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_start_writing_raw.m)
  """

  return Runtime.call("fiff_start_writing_raw", *args, **kwargs)
