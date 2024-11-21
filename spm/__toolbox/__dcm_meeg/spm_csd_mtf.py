from spm.__wrapper__ import Runtime


def spm_csd_mtf(*args, **kwargs):
    """
      Spectral response of a NMM (transfer function x noise spectrum)  
        FORMAT [y,w,s,g] = spm_csd_mtf(P,M,U)  
        FORMAT [y,w,s,g] = spm_csd_mtf(P,M)  
         
        P - parameters  
        M - neural mass model structure  
        U - trial-specific effects (induces expansion around steady state)  
         
        y - {y(N,nc,nc}} - cross-spectral density for nc channels {trials}  
                         - for N frequencies in M.Hz [default 1:64Hz]  
        w - frequencies  
        s - modulation transfer functions (complex)  
        g - normalised modulation transfer function (true Granger causality)  
         
        When called with U this function will return a cross-spectral response  
        for each of the condition-specific parameters specified in U.X; otherwise  
        it returns the complex CSD for the parameters in P (using the expansion  
        point supplied in M.x)  
         
        When the observer function M.g is specified the CSD response is  
        supplemented with channel noise in sensor space; otherwise the CSD  
        pertains to hidden states.  
         
        NB: requires M.u to specify the number of endogenous inputs  
        This routine and will solve for the (hidden) steady state and use it as  
        the expansion point for subsequent linear systems analysis (if trial  
        specific effects are specified).  
         
        See also:  
         spm_ccf2csd.m, spm_ccf2mar, spm_csd2ccf.m, spm_csd2mar.m, spm_mar2csd.m,  
         spm_csd2coh.m, spm_dcm_mtf.m, spm_Q.m, spm_mar.m and spm_mar_spectral.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_csd_mtf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_csd_mtf", *args, **kwargs)
