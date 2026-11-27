from spm._runtime import Runtime


def _fif2grad(*args, **kwargs):
    r"""
      FIF2GRAD constructs a gradiometer definition from a Neuromag *.fif file  
        The resulting gradiometer definition can be used by Fieldtrip for forward  
        and inverse computations.  
         
        Use as  
        grad = fif2grad(filename)  
         
        See also CTF2GRAD, BTI2GRAD, MNE2GRAD, ITAB2GRAD, YOKOGAWA2GRAD,  
        FT_READ_SENS, FT_READ_HEADER  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/fif2grad.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fif2grad", *args, **kwargs)
