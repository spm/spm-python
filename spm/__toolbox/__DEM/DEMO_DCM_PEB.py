from spm.__wrapper__ import Runtime


def DEMO_DCM_PEB(*args, **kwargs):
    """
      Test routine to check group DCM for electrophysiology  
       --------------------------------------------------------------------------  
        This routine illustrates the use of Bayesian model reduction when  
        inverting hierarchical (dynamical) models; for example, multisubject DCM  
        models. In this context, we have hierarchical models that are formally  
        similar to parametric empirical Bayesian models - with the exception  
        that the model of the first level can be nonlinear and dynamic. In brief,  
        this routine shows how to finesse the brittleness of Bayesian model  
        comparison at the single subject level by equipping the model with an  
        extra (between subject) level. It illustrates the recovery of group  
        effects on modulatory changes in effective connectivity (in the mismatch  
        negativity paradigm) - based upon real data.  
         
        First, an EEG DCM (using empirical grand mean data) is inverted to  
        find plausible group mean parameters. Single subject data are  
        then generated using typical within and between subject variance (here,  
        group differences in the modulation of intrinsic connectivity. We then  
        illustrate a variety of Bayesian model averaging and reduction procedures  
        to recover the underlying group effects.  
         
        See also: spm_dcm_bmr, spm_dcm_peb and spm_dcm_peb_bma  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEMO_DCM_PEB.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEMO_DCM_PEB", *args, **kwargs, nargout=0)
