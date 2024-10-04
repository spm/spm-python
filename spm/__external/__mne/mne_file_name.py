from spm.__wrap__ import _Runtime


def mne_file_name(*args, **kwargs):
  """   
      [name] = mne_file_name(dir,name)  
     
      Compose a file name under MNE_ROOT  
     
      dir     - Name of the directory containing the file name  
      name    - Name of the file under that directory  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_file_name.m)
  """

  return _Runtime.call("mne_file_name", *args, **kwargs)
