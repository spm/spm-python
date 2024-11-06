from spm.__wrapper__ import Runtime


def spm_COVID_BMR(*args, **kwargs):
    """
      Bayesian model reduction for COVID models  
        FORMAT spm_COVID_BMR(DCM)  
        DCM - dynamic causal model for covid outbreak  
         
        This subroutine applies Bayesian model reduction to a DCM for the corona  
        virus outbreak, asking whether any parameters can be treated as fixed  
        parameters by reducing its prior variance to 0. Finally, the optimum  
        priors are identified by applying discrete levels of shrinkage priors to  
        each parameter.  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_COVID_BMR.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_COVID_BMR", *args, **kwargs, nargout=0)
