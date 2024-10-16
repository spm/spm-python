from spm.__wrapper__ import Runtime


def fiff_start_file(*args, **kwargs):
  """   
    [fid] = fiff_start_file(name)  
      
    Opens a fif file for writing and writes the compulsory header tags  
     
        name           The name of the file to open. It is recommended  
                       that the name ends with .fif  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/fiff_start_file.m)
  """

  return Runtime.call("fiff_start_file", *args, **kwargs)
