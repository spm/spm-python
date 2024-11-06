from spm.__wrapper__ import Runtime


def spm_eeg_inv_vbecd_getLF(*args, **kwargs):
    """
      Estimation of the leadfield matrix and its spatial derivative if required   
        for a set of dipoles used in the VB-ECD solution  
        Scales non-eeg data up by a fixed factor (1e8) for compatibility of  
        units  
         
        FORMAT [gmn, gm, dgm] = spm_eeg_inv_vbecd_getLF(s, sens, vol, step)  
          
        s      - location vector  
        sens   - sensor locations (MNI [mm])  
        vol    - volume structure needed by fieldtrip  
        step   - stepsize to compute numerical derivatives  
         
        gmn    - leadfields (three vectors for each dipole)  
        gm     - vectorized leadfields  
        dgm    - vectorized partials wrt locations  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_inv_vbecd_getLF.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_inv_vbecd_getLF", *args, **kwargs)
