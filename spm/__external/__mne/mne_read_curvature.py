from spm._runtime import Runtime


def mne_read_curvature(*args, **kwargs):
    r"""
       
        [curf] = mne_read_surface(fname)  
         
        Reads a FreeSurfer curvature file  
         
        fname       - The file to read  
        curv        - The curvature values  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_read_curvature.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_read_curvature", *args, **kwargs)
