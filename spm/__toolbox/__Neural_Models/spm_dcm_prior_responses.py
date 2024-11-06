from spm.__wrapper__ import Runtime


def spm_dcm_prior_responses(*args, **kwargs):
    """
      Demo routine that computes transfer functions for free parameters  
       ==========================================================================  
         
        This routine provides a survey of responses under stationarity  
        assumptions for the suite of neural mass and mean field models used in  
        DCM. It characterises the steady-state responses - under prior  
        expectations - using spectral density and autocovariance functions  
        with and with out channel noise. it then proceeds to evaluate evoked  
        responses to a canonical input.  
         
        This function is used primarily to check the prior expectations to ensure  
        the expected responses within a comparable and appropriate range for  
        scale empirical data. The amplitude of the responses are set by the  
        scaling of U in the equations of motion for each model.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/spm_dcm_prior_responses.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_prior_responses", *args, **kwargs, nargout=0)
