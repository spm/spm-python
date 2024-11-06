from spm.__wrapper__ import Runtime


def spm_dcm_average(*args, **kwargs):
    """
      Produce an aggregate DCM model using Bayesian FFX averaging  
        FORMAT [DCM] = spm_dcm_average(P,name,nocond,graphics)  
         
        P         -  character/cell array of DCM filenames  
        name      -  name of DCM output file (will be prefixed by 'DCM_avg_')  
        nocond    -  optional flag for suppressing conditional dependencies  
        graphics  -  optional flag for showing outliers (based on conditional  
                     entropy)  
         
        This routine creates a new DCM in which the parameters are averaged  
        over a number of fitted DCM models. These can be over sessions or over  
        subjects. This average model can then be interrogated using the standard  
        DCM 'review' options to look at contrasts of parameters. The resulting  
        inferences correspond to a Bayesian Fixed Effects analysis. If called with  
        no output arguments the Bayesian parameter average DCM will be written to  
        file, otherwise the DCM structure is returned.  
         
        Note that the Bayesian averaging is only applied to the A, B and C  
        matrices (and matrix D if a nonlinear model is used).  
        All other quantities in the average model are initially simply copied from  
        the first DCM in the list. Subsequently, they are deleted before saving  
        the average DCM in order to avoid any false impression that averaged  
        models could be used for model comparison or contained averaged time series.  
        Neither operation is valid and will be prevented by the DCM interface.  
        Finally, note that only models with exactly the same A,B,C,(D) structure  
        and the same brain regions can be averaged.  
         
        A Bayesian random effects analysis can be implemented for a particular  
        contrast using the spm_dcm_sessions.m function.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_average.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_average", *args, **kwargs)
