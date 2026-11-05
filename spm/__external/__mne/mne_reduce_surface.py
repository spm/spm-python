from spm._runtime import Runtime


def mne_reduce_surface(*args, **kwargs):
    r"""
       
         [verts, faces] = mne_reduce_surface(surfin,desired_ntri,surfout)  
         
         verts       - Vertex coordinates in meters  
         faces       - The triangulation information  
         
         surfin      - Name of a surface file to read  
         desired_nri - Desired number of triangles after reduction  
         surfout     - Name of a surface file to hold the reduce surface (optional)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_reduce_surface.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_reduce_surface", *args, **kwargs)
