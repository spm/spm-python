from spm.__wrap__ import _Runtime


def mne_write_surface(*args, **kwargs):
  """   
    mne_write_surface(fname,verts,faces)  
     
    Writes a FreeSurfer surface file  
     
    fname       - The file to write  
    verts       - Vertex coordinates in meters  
    faces       - The triangle descriptions  
    comment     - Optional comment to include  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_write_surface.m)
  """

  return _Runtime.call("mne_write_surface", *args, **kwargs, nargout=0)
