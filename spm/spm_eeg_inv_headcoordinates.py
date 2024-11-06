from spm.__wrapper__ import Runtime


def spm_eeg_inv_headcoordinates(*args, **kwargs):
    """
      Returns the homogeneous coordinate transformation matrix  
        that converts the specified fiducials in any coordinate system (e.g. MRI)  
        into the rotated and translated headccordinate system.  
         
        FORMAT M1 = spm_eeg_inv_headcoordinates(nas, lpa, rpa)  
         
        The headcoordinate system in CTF is defined as follows:  
        the origin is exactly between lpa and rpa  
        the X-axis goes towards nas  
        the Y-axis goes approximately towards lpa, orthogonal to X and in the plane spanned by the fiducials  
        the Z-axis goes approximately towards the vertex, orthogonal to X and Y  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_inv_headcoordinates.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_inv_headcoordinates", *args, **kwargs)
