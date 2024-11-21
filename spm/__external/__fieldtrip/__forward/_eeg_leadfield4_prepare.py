from spm.__wrapper__ import Runtime


def _eeg_leadfield4_prepare(*args, **kwargs):
    """
      EEG_LEADFIELD4_PREPARE computes constant factors for series expansion  
        for the 4 concentric sphere electric leadfield computation. Calling  
        this function speeds up subsequent computations, as the constant  
        factors "t" do not have to be computed each time in eeg_leadfield4.  
         
        Use as  
          vol.t = eeg_leadfield4_prepare(vol, order);  
        where  
          vol.r      radius of the 4 spheres   
          vol.cond   conductivity of the 4 spheres  
        and N is the number of terms for the series (default 60).   
         
        The center of the spheres should be at the origin.  
         
        This implementation is adapted from  
          Lutkenhoner, Habilschrift 1992.  
        which again is taken from  
          B. N. Cuffin and D. Cohen. Comparion of the Magnetoencephalogram and the Electroencephalogram. Electroencephalogr Clin Neurophysiol, 47:131-146, 1979.  
         
        See also EEG_LEADFIELD4  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/eeg_leadfield4_prepare.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("eeg_leadfield4_prepare", *args, **kwargs)
