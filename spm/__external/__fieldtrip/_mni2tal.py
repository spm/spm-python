from spm.__wrapper__ import Runtime


def _mni2tal(*args, **kwargs):
    """
      Converts coordinates from MNI brain to best guess  
        for equivalent Talairach coordinates  
        FORMAT outpoints = mni2tal(inpoints)  
        Where inpoints is N by 3 or 3 by N matrix of coordinates  
         (N being the number of points)  
        outpoints is the coordinate matrix with Talairach points  
        Matthew Brett 10/8/99  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/mni2tal.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mni2tal", *args, **kwargs)
