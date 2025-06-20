from spm._runtime import Runtime


def mne_read_curvature(*args, **kwargs):
    """
       
        [curf] = mne_read_surface(fname)  
         
        Reads a FreeSurfer curvature file  
         
        fname       - The file to read  
        curv        - The curvature values  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_read_curvature.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_read_curvature", *args, **kwargs)
