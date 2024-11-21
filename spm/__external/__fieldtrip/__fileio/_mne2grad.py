from spm.__wrapper__ import Runtime


def _mne2grad(*args, **kwargs):
    """
      MNE2GRAD converts a header from a fif file that was read using the MNE toolbox into  
        a gradiometer structure that can be understood by the FieldTrip low-level forward  
        and inverse routines.  
         
        Use as  
          [grad, elec] = mne2grad(hdr, dewar, coilaccuracy)  
        where  
          dewar        = boolean, whether to return it in dewar or head coordinates (default = false, i.e. head coordinates)  
          coilaccuracy = empty or a number (default = [])  
          coildeffile  = empty or a filename of a valid coil_def.dat file  
         
        See also CTF2GRAD, BTI2GRAD  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/mne2grad.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mne2grad", *args, **kwargs)
