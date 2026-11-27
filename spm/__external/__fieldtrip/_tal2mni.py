from spm._runtime import Runtime


def _tal2mni(*args, **kwargs):
    r"""
      Converts coordinates to MNI brain best guess  
        from Talairach coordinates  
        FORMAT outpoints = tal2mni(inpoints)  
        Where inpoints is N by 3 or 3 by N matrix of coordinates  
         (N being the number of points)  
        outpoints is the coordinate matrix with MNI points  
        Matthew Brett 2/2/01  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/tal2mni.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("tal2mni", *args, **kwargs)
