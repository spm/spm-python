from spm.__wrapper__ import Runtime


def DEMO_DCM_PEB_FIT(*args, **kwargs):
    """
      Test routine to check group DCM for electrophysiology  
       --------------------------------------------------------------------------  
        This routine illustrates the use of Bayesian model reduction when  
        inverting hierarchical (dynamical) models; for example, multisubject DCM  
        models. In this demonstration empirical Bayesian model reduction is  
        applied recursively in an attempt to finesse the local  minimum problem  
        with a nonlinear DCMs. The estimates are compared against standard  
        Bayesian model reduction, in terms of the subject specific estimates and  
        Bayesian model comparison  (and averages) at the between subject level.  
         
        This demo considers a single goup (e.g., of normal subjects) and the  
        differences between the group average using emprical Bayesian reduction  
        and the Bayesian reduction of the (grand) average response.  
         
        See also: DEMO_DCM_PEB_REC.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEMO_DCM_PEB_FIT.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEMO_DCM_PEB_FIT", *args, **kwargs, nargout=0)
