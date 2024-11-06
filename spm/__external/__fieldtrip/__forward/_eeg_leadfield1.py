from spm.__wrapper__ import Runtime


def _eeg_leadfield1(*args, **kwargs):
    """
      EEG_LEADFIELD1 electric leadfield for a dipole in a single sphere  
         
        [lf] = eeg_leadfield1(R, elc, vol)  
         
        with input arguments  
          R         position dipole (vector of length 3)  
          elc       position electrodes  
        and vol being a structure with the elements  
          vol.r     radius of sphere  
          vol.cond  conductivity of sphere  
         
        The center of the sphere should be at the origin.  
         
        This implementation is adapted from  
          Luetkenhoener, Habilschrift '92  
        The original reference is  
          R. Kavanagh, T. M. Darccey, D. Lehmann, and D. H. Fender. Evaluation of methods  
          for three-dimensional localization of electric sources in the human brain. IEEE  
          Trans Biomed Eng, 25:421-429, 1978.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/eeg_leadfield1.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("eeg_leadfield1", *args, **kwargs)
