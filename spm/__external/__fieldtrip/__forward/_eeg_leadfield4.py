from spm.__wrapper__ import Runtime


def _eeg_leadfield4(*args, **kwargs):
    """
      EEG_LEADFIELD4 electric leadfield for a dipole in 4 concentric spheres  
          
        [lf] = eeg_leadfield4(R, elc, vol)  
         
        with input arguments  
          R          position of the dipole  
          elc        position of the electrodes  
        and vol being a structure with the elements  
          vol.r      radius of the 4 spheres   
          vol.cond   conductivity of the 4 spheres  
          vol.t      constant factors for series expansion (optional)  
         
        The center of the spheres should be at the origin.  
         
        This implementation is adapted from  
          Lutkenhoner, Habilschrift 1992.  
        The original reference is  
         Cuffin BN, Cohen D. Comparison of the magnetoencephalogram and electroencephalogram. Electroencephalogr Clin Neurophysiol. 1979 Aug;47(2):132-46.   
         
        See also EEG_LEADFIELD4_PREPARE for precomputing the constant factors,  
        which can save time when multiple leadfield computations are done.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/eeg_leadfield4.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("eeg_leadfield4", *args, **kwargs)
