from spm.__wrapper__ import Runtime


def spm_dcm_fmri_mode_gen(*args, **kwargs):
    """
      Generate adjacency matrix for spectral DCM from Lyapunov exponents  
        FORMAT [Ep,Cp] = spm_dcm_fmri_mode_gen(Ev,modes,Cv)  
        Ev    - Lyapunov exponents or eigenvalues of effective connectivity  
        modes - modes or eigenvectors  
        Cv    - optional (posterior) covariance matrix  
         
        Ep    - Jacobian or (symmetric) effective connectivity matrix  
        Cp    - posterior covariance matrix of Jacobian elements  
         
        This routine computes the connecivity graph for spectral DCM (modes).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_fmri_mode_gen.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_fmri_mode_gen", *args, **kwargs)
