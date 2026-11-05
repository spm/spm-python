from spm._runtime import Runtime


def _ricoh2grad(*args, **kwargs):
    r"""
      RICOH2GRAD converts the position and weights of all coils that  
        compromise a gradiometer system into a structure that can be used  
        by FieldTrip. This implementation uses the "ricoh_meg_reader" toolbox.  
         
        See also FT_READ_HEADER, CTF2GRAD, BTI2GRAD, FIF2GRAD, YOKOGAWA2GRAD_NEW  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/ricoh2grad.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ricoh2grad", *args, **kwargs)
