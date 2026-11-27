from spm._runtime import Runtime


def _itab2grad(*args, **kwargs):
    r"""
      ITAB2GRAD converts the original Chieti ITAB header structure into  
        a gradiometer definition that is compatible with FieldTrip forward  
        and inverse computations  
         
        See also CTF2GRAD, BTI2GRAD, FIF2GRAD, MNE2GRAD, YOKOGAWA2GRAD,  
        FT_READ_SENS, FT_READ_HEADER  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/itab2grad.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("itab2grad", *args, **kwargs)
