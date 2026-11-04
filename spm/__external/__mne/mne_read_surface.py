from spm._runtime import Runtime


def mne_read_surface(*args, **kwargs):
    r"""
       
        [verts, faces] = mne_read_surface(fname)  
         
        Reads a FreeSurfer surface file  
         
        fname       - The file to read  
        verts       - Vertex coordinates in meters  
        faces       - The triangle descriptions  
                      NOTE: The quad file faces are split by this routine to  
                      create triangular meshes for all files  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_read_surface.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_read_surface", *args, **kwargs)
