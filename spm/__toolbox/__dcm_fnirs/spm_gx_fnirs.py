from spm.__wrapper__ import Runtime


def spm_gx_fnirs(*args, **kwargs):
    """
      fNIRS optics equation  
        FORMAT [g] = spm_gx_fnirs(x,u,P,M)  
         
        x   - state vector     (see spm_fx_fnirs)  
        u   - experimental inputs  
        P   - prior of latent variables  
        M   - model structure  
         
        g   - optical density changes  
       __________________________________________________________________________  
        References for optics equations:  
        1. Arridge, SR 1999. Optical tomography in medical imaging. Inverse Prob.  
        15: R41-R93.  
        2. Gagnon L, Yucel, MA, Dehaes, M, Cooper, RJ, Perdue, KL, Selb, J, Huppert TJ,  
        Hoge RD, Boas DA, 2012. Quantification of the cortical contribution to  
        the NIRS signal over NIRS-fMRI measurements. NeuroImage 59: 3933-3940.  
        3. Tak, S, Kempny, AM, Friston, KJ, Leff, AP, Penny WD, Dynamic causal  
        modelling for functional near-infrared spectroscopy. NeuroImage 111: 338-349.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_fnirs/spm_gx_fnirs.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_gx_fnirs", *args, **kwargs)
