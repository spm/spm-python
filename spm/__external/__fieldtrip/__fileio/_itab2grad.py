from spm.__wrapper__ import Runtime


def _itab2grad(*args, **kwargs):
    """
      ITAB2GRAD converts the original Chieti ITAB header structure into  
        a gradiometer definition that is compatible with FieldTrip forward  
        and inverse computations  
         
        See also CTF2GRAD, BTI2GRAD, FIF2GRAD, MNE2GRAD, YOKOGAWA2GRAD,  
        FT_READ_SENS, FT_READ_HEADER  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/itab2grad.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("itab2grad", *args, **kwargs)
