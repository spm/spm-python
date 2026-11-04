from spm._runtime import Runtime


def _volumepermute(*args, **kwargs):
    r"""
      VOLUMEPERMUTE  
         
        See also VOLUMEFLIP, ALIGN_IJK2XYZ, ALIGN_XYZ2IJK  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/volumepermute.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("volumepermute", *args, **kwargs)
