from spm._runtime import Runtime


def DEM_get_faces(*args, **kwargs):
    r"""
      Utility routine to load images and create basis functions using a  
        discrete cosine basis set (over a feature dimension). This is written  
        specifically for the images used in this demonstration and should be  
        tailored for any new images.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_get_faces.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_get_faces", *args, **kwargs, nargout=0)
