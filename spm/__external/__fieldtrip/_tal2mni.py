from spm.__wrapper__ import Runtime


def _tal2mni(*args, **kwargs):
    """
      Converts coordinates to MNI brain best guess  
        from Talairach coordinates  
        FORMAT outpoints = tal2mni(inpoints)  
        Where inpoints is N by 3 or 3 by N matrix of coordinates  
         (N being the number of points)  
        outpoints is the coordinate matrix with MNI points  
        Matthew Brett 2/2/01  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/tal2mni.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("tal2mni", *args, **kwargs)
