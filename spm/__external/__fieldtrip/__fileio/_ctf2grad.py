from spm.__wrapper__ import Runtime


def _ctf2grad(*args, **kwargs):
    """
      CTF2GRAD converts a CTF header to a gradiometer structure that can be understood by  
        the FieldTrip low-level forward and inverse routines. The fieldtrip/fileio  
        read_header function can use three different implementations of the low-level code  
        for CTF data. Each of these implementations is dealt with here.  
         
        Use as  
          [grad, elec] = ctf2grad(hdr, dewar, coilaccuracy)  
        where  
          dewar        = boolean, whether to return it in dewar or head coordinates (default is head coordinates)  
          coilaccuracy = empty or a number (default is empty)  
          coildeffile  = empty or a filename of a valid coil_def.dat file  
         
        See also BTI2GRAD, FIF2GRAD, MNE2GRAD, ITAB2GRAD, YOKOGAWA2GRAD,  
        FT_READ_SENS, FT_READ_HEADER  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/ctf2grad.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ctf2grad", *args, **kwargs)
