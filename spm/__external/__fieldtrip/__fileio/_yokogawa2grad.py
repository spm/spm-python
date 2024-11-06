from spm.__wrapper__ import Runtime


def _yokogawa2grad(*args, **kwargs):
    """
      YOKOGAWA2GRAD converts the position and weights of all coils that  
        compromise a gradiometer system into a structure that can be used  
        by FieldTrip. This implementation uses the old "yokogawa" toolbox.  
         
        See also CTF2GRAD, BTI2GRAD, FIF2GRAD, MNE2GRAD, ITAB2GRAD,  
        FT_READ_SENS, FT_READ_HEADER  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/yokogawa2grad.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("yokogawa2grad", *args, **kwargs)
