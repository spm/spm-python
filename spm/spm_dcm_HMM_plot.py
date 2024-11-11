from spm.__wrapper__ import Runtime


def spm_dcm_HMM_plot(*args, **kwargs):
    """
      Plot the results of a hidden Markov model of state transitions in the DCM  
        FORMAT spm_dcm_HMM_plot(HMM,s)  
          
        HMM(s)  
            HMM(s).X  - posterior expectation of hidden states  
            HMM(s).qB - posterior expectation of HMM parameters  
            HMM(s).qb - and Dirichlet concentration parameters  
            HMM(s).qP - posterior expectation of PEB parameters  
            HMM(s).qC - posterior covariances of PEB parameters  
            HMM(s).iP - indices of DCM parameters  
            HMM(s).Ep - posterior expectation of DCM parameters  
            HMM(s).Cp - posterior covariances of DCM parameters  
            HMM(s).L  - free energy components  
            HMM(s).F  - total free energy (model evidence)  
         
        s  -  index of HMM structure (number of hidden states)  
              [default: HMM(end)]  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_HMM_plot.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_HMM_plot", *args, **kwargs, nargout=0)
