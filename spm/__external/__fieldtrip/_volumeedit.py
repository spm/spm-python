from spm._runtime import Runtime


def _volumeedit(*args, **kwargs):
    r"""
      VOLUMEEDIT allows for editing of a (booleanized) volume, in order to  
        remove unwanted voxels. Interaction proceeds with the keyboard and the  
        mouse.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/volumeedit.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("volumeedit", *args, **kwargs)
