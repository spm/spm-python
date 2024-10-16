from spm.__wrapper__ import Runtime


def mne_reduce_surface(*args, **kwargs):
  """   
     [verts, faces] = mne_reduce_surface(surfin,desired_ntri,surfout)  
     
     verts       - Vertex coordinates in meters  
     faces       - The triangulation information  
     
     surfin      - Name of a surface file to read  
     desired_nri - Desired number of triangles after reduction  
     surfout     - Name of a surface file to hold the reduce surface (optional)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_reduce_surface.m)
  """

  return Runtime.call("mne_reduce_surface", *args, **kwargs)
