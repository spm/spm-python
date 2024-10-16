from spm.__wrapper__ import Runtime


def mne_read_curvature(*args, **kwargs):
  """   
    [curf] = mne_read_surface(fname)  
     
    Reads a FreeSurfer curvature file  
     
    fname       - The file to read  
    curv        - The curvature values  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_read_curvature.m)
  """

  return Runtime.call("mne_read_curvature", *args, **kwargs)
