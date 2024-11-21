from spm.__wrapper__ import Runtime


def spm_dcm_diagnose(*args, **kwargs):
    """
      Post hoc diagnosis of DCMs (under the Laplace approximation)  
        FORMAT spm_dcm_diagnose(DCM,'field','field',...)  
         
        DCM        - DCM stricture (inverted)  
        field      - field name(s) of parameters to consider  
         
       --------------------------------------------------------------------------  
        This routine searches over all possible reduced models of a full model  
        (DCM) and uses post hoc model selection to select the best. Reduced  
        models mean all permutations of free parameter sets (parameters with non-  
        zero prior covariance), where models are defined in terms of their prior  
        covariance. The full model should be inverted prior to post hoc  
        optimization. If there are more than 8 free-parameter sets, this routine  
        will implement a greedy search: This entails searching over all  
        permutations of the 8 sets whose removal (shrinking the prior  
        variance to zero) produces the smallest reduction (greatest increase)  
        in model evidence. This procedure is repeated until all sets  
        are retained in the best model or there are no more parameters to  
        consider.  
         
        A parameter set is specified implicitly by the structure (DCM.Ep). Each  
        set corresponds to a column of (the cell arrays or matrix) each field of  
        DCM.Ep.  
         
        if only one field is specified the log-evidence is computed as a function  
        of the scaled prior variance. Redundant parameters have a log-evidence   
        that keeps increasing as the prior variance shrinks.  
         
        The outputs of this routine are graphics reporting the model reduction  
        (optimisation). Red means weak evidence; blue strong evidence (> 3) and   
        cyan very strong evidence (> 5)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_diagnose.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_diagnose", *args, **kwargs)
