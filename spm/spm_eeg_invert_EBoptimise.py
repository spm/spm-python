from spm.__wrapper__ import Runtime


def spm_eeg_invert_EBoptimise(*args, **kwargs):
    """
      function [F,M,Cq,Cp,QE,Qp] = spm_eeg_invert_EBoptimise(AY,UL,opttype,Qp,Qe,Qe0)  
        Empirical Bayes optimization of priors Qp and Qe to fit data AY based on lead fields UL  
        AY concatenated dimension reduced trials of M/EEG data  
        UL dimension reduced lead field  
        Qp source level priors- where Qp{i}.q holds an eigenmode. So source covariance  
                               component is Qp{i}.q*Qp{i}.q'.  
                                Alternately Qp{i} could be full source covariance component  
        Qe sensor noise prior  
        Qe0 floor of noise power to signal power (posteiror estimate of sensor noise will always be at  
        least this big)  
        opttype- how to optimize 'ARD','GS' or 'REML'  
        QE sensor noise posterior  
        Cp source level posterior (source by source variance)  
        F free energy  
        M MAP operator  
        Cq conditional variance  
        F free energy  
        Qp contains the posterior in same form as prior  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_invert_EBoptimise.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_invert_EBoptimise", *args, **kwargs)
