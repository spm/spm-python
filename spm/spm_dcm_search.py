from spm.__wrapper__ import Runtime


def spm_dcm_search(*args, **kwargs):
    """
      Post hoc optimisation of DCMs (under Laplace approximation)  
        FORMAT spm_dcm_search(P)  
         
        P         -  character/cell array of DCM filenames  
         
       --------------------------------------------------------------------------  
        spm_dcm_search operates on different DCMs of the same data to identify  
        the best model. It will invert the full model whose free-parameters are  
        the union (superset) of all free parameters in each model specified. The  
        routine then uses a post hoc selection procedure to evaluate the log-  
        evidence and conditional density over free-parameters of each model  
        specified.  
         
        The DCM specified does not need to be estimated. spm_dcm_search will   
        invert the requisite (full DCM) automatically.  
         
        The outputs of this routine are graphics reporting the model space search  
        (optimisation) and a DCM_optimum (in the first DCMs directory) for the  
        best DCM. The structural and function (spectral embedding) graphs are  
        based on this DCM.  
         
        DCM_optimum  contains the fields:  
               DCM.P   - character/cell array of DCM filenames  
               DCM.PF  - their associated free energies  
               DCM.PP  - and posterior (model) probabilities  
         
        In addition, the free energies and posterior estimates of each DCM in P   
        are saved for subsequent searches over different partitions of model   
        space.  
         
        See also: spm_dcm_post_hoc.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_search.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_search", *args, **kwargs, nargout=0)
