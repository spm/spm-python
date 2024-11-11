from spm.__wrapper__ import Runtime


def DEM_get_faces(*args, **kwargs):
    """
      Utility routine to load images and create basis functions using a  
        discrete cosine basis set (over a feature dimension). This is written  
        specifically for the images used in this demonstration and should be  
        tailored for any new images.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_get_faces.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_get_faces", *args, **kwargs, nargout=0)
