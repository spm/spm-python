from spm.__wrapper__ import Runtime


def spm_dcm_peb_rnd_search(*args, **kwargs):
    """
      Re-randomisation testing for empirical Bayes and DCM  
        FORMAT [BMC,M] = spm_dcm_peb_rnd_search(DCM,M,field)  
         
        DCM   - {N x 1} structure DCM array of (M) DCMs from (N) subjects  
        -------------------------------------------------------------------  
            DCM{i}.M.pE - prior expectation of parameters  
            DCM{i}.M.pC - prior covariances of parameters  
            DCM{i}.Ep   - posterior expectations  
            DCM{i}.Cp   - posterior covariance  
         
        M.X    - second level design matrix, where X(:,1) = ones(N,1) [default]  
        M.pE   - second level prior expectation of parameters  
        M.pC   - second level prior covariances of parameters  
        M.hE   - second level prior expectation of log precisions  
        M.hC   - second level prior covariances of log precisions  
        M.Q    - covariance components: {'single','fields','all','none'}  
         
        field  - parameter fields in DCM{i}.Ep to optimise [default: {'A','B'}]  
                 'All' will invoke all fields  
          
        BMC    - Bayesian model comparison structure   
        -------------------------------------------------------------  
            BMC.F    - free energy over joint model space  
            BMC.P    - posterior probability over models  
            BMC.Px   - posterior probability over 1st level models  
            BMC.Pw   - posterior probability over 2nd level models  
            BMC.M    - second level model  
            BMC.K    - model space  
       __________________________________________________________________________  
         
        This routine calls spm_dcm_peb_rnd to assess the distribution of log Bayes  
        factors for different hyperpriors on between subject precision. It is  
        assumed that the best hyperpriors maximise the entropy of the null  
        distribution of ensuing p-values. This type of prior is then used to  
        perform Bayesian model comparison. The optimised priors are in the second  
        level model (M.hE, M.hC) in the output arguments.  
         
        See also: spm_dcm_peb_rnd.m and spm_dcm_loo.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_peb_rnd_search.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_peb_rnd_search", *args, **kwargs)
