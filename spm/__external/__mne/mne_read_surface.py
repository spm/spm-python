from spm.__wrap__ import _Runtime


def mne_read_surface(*args, **kwargs):
  """   
    [verts, faces] = mne_read_surface(fname)  
     
    Reads a FreeSurfer surface file  
     
    fname       - The file to read  
    verts       - Vertex coordinates in meters  
    faces       - The triangle descriptions  
                  NOTE: The quad file faces are split by this routine to  
                  create triangular meshes for all files  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_read_surface.m)
  """

  return _Runtime.call("mne_read_surface", *args, **kwargs)
