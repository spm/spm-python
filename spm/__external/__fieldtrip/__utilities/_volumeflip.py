from spm._runtime import Runtime


def _volumeflip(*args, **kwargs):
    r"""
      VOLUMEFLIP  
         
        See also VOLUMEPERMUTE, ALIGN_IJK2XYZ, ALIGN_XYZ2IJK  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/volumeflip.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("volumeflip", *args, **kwargs)
