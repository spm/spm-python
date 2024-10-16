from spm.__wrapper__ import Runtime


def fiff_read_mri(*args, **kwargs):
  """   
    [stack] = fiff_read_mri(fname,read_data)  
     
    read_data argument is optional, if set to false the pixel data are  
    not read. The default is to read the pixel data  
     
    Read a fif format MRI description file  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_read_mri.m)
  """

  return Runtime.call("fiff_read_mri", *args, **kwargs)
