from spm.__wrapper__ import Runtime


def spm_eeg_inv_vbecd(*args, **kwargs):
    """
      Model inversion routine for ECDs using variational Bayesian approach  
         
        FORMAT P = spm_eeg_inv_vbecd(P)  
         
        Input:  
        structure P with fields:  
         forward      - structure containing the forward model, i.e. the "vol"  
                        and "sens" structure in a FT compatible format  
         bad          - list of bad channels, not to use.  
         y            - data vector  
         
         Niter        - maximum number of iterations  
         priors       - priors on parameters,  as filled in (and  
                        described) in spm_eeg_inv_vbecd_gui.m.  
         
        Output:  
        same structure with extra fields  
         init         - initial values used for mu_w/s  
         dF           - successive (relative) improvement of F  
         post         - posterior value of estimated parameters and their variance  
         Fi           - successive values of F  
         F            - Free energy final value.  
         
        Reference:  
        Kiebel et al., Variational Bayesian inversion of the equivalent current  
        dipole model in EEG/MEG., NeuroImage, 39:728-741, 2008  
        (Although this algorithm uses a function for general Bayesian inversion of  
        a non-linear model - see spm_nlsi_gn)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_inv_vbecd.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_inv_vbecd", *args, **kwargs)
