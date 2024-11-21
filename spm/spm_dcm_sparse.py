from spm.__wrapper__ import Runtime


def spm_dcm_sparse(*args, **kwargs):
    """
      Bayesian model reduction of all permutations of model parameters  
        FORMAT [Ep,Cp] = spm_dcm_sparse(DCM,field)  
         
        DCM      - A single estimated DCM (or PEB) structure:  
         
         DCM.M.pE  - prior expectation  
         DCM.M.pC  - prior covariance  
         DCM.Ep    - posterior expectation  
         DCM.Cp    - posterior covariances  
         DCM.gamma - prior variance    of reduced parameters (default: 0)  
         
        field      - parameter fields in DCM{i}.Ep to optimise [default: {'A','B'}]  
                    'All' will invoke all fields (i.e. random effects)  
                    If Ep is not a structure, all parameters will be considered  
         
        Returns:  
         Ep    - (BMA) posterior expectation  
         Cp    - (BMA) posterior covariance  
         
       --------------------------------------------------------------------------  
        This routine searches over reduced (nested) models of a full model (DCM)  
        using Bayesian model reduction and performs Bayesian Model Averaging.  
        'Reduced' means some free parameters (parameters with a non-  
        zero prior covariance) are switched off by fixing their prior variance  
        to zero.This version incorporates a sparsity  prior over models (with a  
        Gaussian hyperprior). In other words, the free energy is taken to be the  
        likelihood of some data under a given model. The prior on that model  
        corresponds to a softmax function of the prior entropy. Finally, the  
        softmax (Gibbs) parameter is equipped with a Gaussian prior. Using  
        Bayesian model reduction, this routine evaluates the joint probability  
        over model and softmax sparsity parameter. The marginals over model space  
        are then used to form Bayesian model averaging.  
         
        The greedy search in this version simply evaluates the log evidence of  
        models with and without each parameter and then successively removes the  
        parameters with the least evidence.  
         
        See also: spm_dcm_bmr and spm_dcm_bmr_all  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_sparse.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_sparse", *args, **kwargs)
