from spm.__wrapper__ import Runtime


def mne_read_surface(*args, **kwargs):
    """
       
        [verts, faces] = mne_read_surface(fname)  
         
        Reads a FreeSurfer surface file  
         
        fname       - The file to read  
        verts       - Vertex coordinates in meters  
        faces       - The triangle descriptions  
                      NOTE: The quad file faces are split by this routine to  
                      create triangular meshes for all files  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_read_surface.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mne_read_surface", *args, **kwargs)
