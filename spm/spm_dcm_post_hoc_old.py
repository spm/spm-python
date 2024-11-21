from spm.__wrapper__ import Runtime


def spm_dcm_post_hoc_old(*args, **kwargs):
    """
      Post hoc optimisation of DCMs (under the Laplace approximation)  
        FORMAT DCM = spm_dcm_post_hoc(P,fun,field,field,...)  
         
        P         - character/cell array of DCM filenames  
                  - or cell array of DCM structures; where  
         DCM.M.pE - prior expectation (with parameters in pE.A, pE.B and pE.C)  
         DCM.M.pC - prior covariance  
         DCM.Ep   - posterior expectations  
         DCM.Cp   - posterior covariance  
         
        fun       - optional family definition function: k = fun(A,B,C)  
                    k = 1,2,...,K for K families or proper subsets of a partition  
                    of model space - a function of the adjacency matrices: e.g.,  
         
                    fun = @(A,B,C) any(spm_vec(B(:,:,2))) + 1;  
         
                    returns 1 if there are no bilinear parameters for the 2nd  
                    bilinear effect and 2 if there are. fun should be an inline  
                    function or script. NB: Model posteriors over families with  
                    and without free parameters (in A,B,C and D) are evaluated  
                    automatically and saved in DCM_BPA (DCM.Pp)  
         
        field     - the field nsmes of the parameters in the structure pE and Ep   
                    that are to be inlcudied in Baysian model reduction.  
                    The default is the cell array 'A','B','C'  
         
       --------------------------------------------------------------------------  
        This routine searches over all possible reduced models of a full model  
        (DCM) and uses post hoc model selection to select the best. Reduced  
        models mean all permutations of free parameters (parameters with a non-  
        zero prior covariance), where models are defined in terms of their prior  
        covariance. The full model should be inverted prior to post hoc  
        optimization. If there are more than 16 free-parameters, this routine  
        will implement a greedy search: This entails searching over all  
        permutations of the 8 parameters whose removal (shrinking the prior  
        variance to zero) produces the smallest reduction (greatest increase)  
        in model evidence. This procedure is repeated until all 8 parameters  
        are retained in the best model or there are no more parameters to  
        consider. When several DCMs are optimized together (as in group studies),  
        they are checked to ensure the same free parameters have been specified  
        and the log-evidences are pooled in a fixed effects fashion.  
         
        This application of post hoc optimization assumes the DCMs that are  
        optimized are the same model of different data. Normally, this would be  
        a full model, in the sense of having the maximum number of free  
        parameters, such that the set of reduced models is as large as possible.  
        In contrast spm_dcm_search operates on different DCMs of the same data  
        to identify the best model, after inverting the full(est) model  
         
        The outputs of this routine are graphics reporting the model reduction  
        (optimisation) and a DCM_opt_??? for every specified DCM that contains  
        reduced conditional parameters estimates (for simplicity, the original  
        kernels and predicted states are retained). The structural and functional  
        (spectral embedding) graphs are based on Bayesian parameter averages  
        over multiple DCMs, which are stored in DCM_BPA.mat. This DCM also  
        contains the posterior probability of models partitioned according to  
        whether a particular parameter exists or not:  
         
        DCM.Pp     -  Model posterior (with and without each parameter)  
        DCM.Ep     -  Bayesian parameter average under selected model  
        DCM.Cp     -  Bayesian parameter covariance under selected model  
        DCM.Pf     -  Model posteriors over user specified families  
        DCM.fun    -  User-specified family definition function  
        DCM.files  -  List of DCM files used for Bayesian averaging  
         
        See also: spm_dcm_search.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_post_hoc_old.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_post_hoc_old", *args, **kwargs)
