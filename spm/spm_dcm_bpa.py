from spm.__wrapper__ import Runtime


def spm_dcm_bpa(*args, **kwargs):
    """
      Produce an aggregate DCM using Bayesian parameter averaging  
        FORMAT [BPA] = spm_dcm_bpa(DCM,nocd)  
         
        DCM  - {N [x M]} structure array of DCMs from N subjects  
        ------------------------------------------------------------  
            DCM{i}.M.pE - prior expectations of P parameters  
            DCM{i}.M.pC - prior covariance  
            DCM{i}.Ep   - posterior expectations  
            DCM{i}.Cp   - posterior covariance  
         
        nocd - optional flag for suppressing conditional dependencies.  
               This is useful when evaluating the BPA of individual (contrasts  
               of) parameters, where the BPA of a contrast should not be confused  
               with the contrast of a BPA.  
         
        BPA  - DCM structure (array) containing Bayesian parameter averages  
        ------------------------------------------------------------  
            BPA.M.pE - prior expectations of P parameters  
            BPA.M.pC - prior covariance  
            BPA.Ep   - posterior expectations  
            BPA.Cp   - posterior covariance  
         
            BPA.Pp   - posterior probability of > 0  
            BPA.Vp   - posterior variance  
            BPA....  - other fields from DCM{1[,:]}  
       __________________________________________________________________________  
         
        This routine creates a new DCM in which the parameters are averaged over  
        a number of fitted DCMs. These can be over sessions or over subjects.  
        This average model can then be interrogated using the standard DCM  
        'review' options to look at contrasts of parameters. The resulting  
        inferences correspond to a Bayesian Fixed Effects analysis. If called  
        with no output arguments the Bayesian parameter average DCM will be  
        written to DCM_BPA.mat; otherwise, the DCM structure is returned as BPA.  
          
        If DCM is an {N x M} array, Bayesian parameter averaging will be  
        applied to each model (i.e., each row) - and BPA becomes a {1 x M} cell   
        array.  
         
        See also spm_dcm_bma.m, spm_dcm_bmr.m and spm_dcm_peb.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_bpa.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_bpa", *args, **kwargs)
