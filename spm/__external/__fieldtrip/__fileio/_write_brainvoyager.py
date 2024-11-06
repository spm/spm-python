from spm.__wrapper__ import Runtime


def _write_brainvoyager(*args, **kwargs):
    """
      helper function to write volumetric data for brainvoyager.  
        this is old code that moved from ft_volumewrite to clean up  
        the high level function a bit. it is assumed that the orientation  
        of the volume is correct.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/write_brainvoyager.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("write_brainvoyager", *args, **kwargs, nargout=0)
