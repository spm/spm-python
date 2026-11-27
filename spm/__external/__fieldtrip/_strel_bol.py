from spm._runtime import Runtime


def _strel_bol(*args, **kwargs):
    r"""
      STREL_BOL constructs a 3D sphere with the specified radius  
        that can be used as structural element in 3D image processing  
         
        See STREL, IMERODE, IMDILATE (image processing toolbox)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/strel_bol.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("strel_bol", *args, **kwargs)
