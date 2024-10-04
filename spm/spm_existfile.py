from spm.__wrap__ import _Runtime


def spm_existfile(*args, **kwargs):
  """  Check if a file exists on disk - a compiled routine  
    FORMAT s = spm_existfile(filename)  
    filename - filename (can also be a relative or full pathname to a file)  
    s        - logical scalar, true if the file exists and false otherwise  
   __________________________________________________________________________  
     
    This compiled routine is equivalent to:  
    >> s = exist(filename,'file') == 2;  
    and was written for speed purposes. The differences in behaviour are that  
    spm_existfile does not look in MATLAB's search path and does not perform  
    tilde '~' expansion.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_existfile.m)
  """

  return _Runtime.call("spm_existfile", *args, **kwargs)
