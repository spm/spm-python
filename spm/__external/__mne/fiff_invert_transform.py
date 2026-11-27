from spm._runtime import Runtime


def fiff_invert_transform(*args, **kwargs):
    r"""
       
        [itrans] = fiff_invert_transform(trans)  
         
        Invert a coordinate transformation  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_invert_transform.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_invert_transform", *args, **kwargs)
