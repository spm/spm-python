from spm._runtime import Runtime


def spm_eeg_inv_vbecd_getLF(*args, **kwargs):
    r"""
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
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_inv_vbecd_getLF.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_inv_vbecd_getLF", *args, **kwargs)
