from spm._runtime import Runtime


def mne_write_surface(*args, **kwargs):
    r"""
       
        mne_write_surface(fname,verts,faces)  
         
        Writes a FreeSurfer surface file  
         
        fname       - The file to write  
        verts       - Vertex coordinates in meters  
        faces       - The triangle descriptions  
        comment     - Optional comment to include  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_write_surface.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_write_surface", *args, **kwargs, nargout=0)
