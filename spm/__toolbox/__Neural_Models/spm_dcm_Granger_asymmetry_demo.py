from spm.__wrapper__ import Runtime


def spm_dcm_Granger_asymmetry_demo(*args, **kwargs):
    """
      Demo routine for induced responses  
       ==========================================================================  
         
        This routine illustrates the effects of changing inhibitory recurrent  
        connections from superficial pyramidal cells on the Granger causality  
        between two sources. Each source is modeled with a canonical microcircuit  
        model equipped with laminar specific forward and backward connections.  
        The first half of this demo computes the expected Granger causality (using  
        parametric and nonparametric estimators) for a range of self connections  
        and then displays the results by plotting the forward  Granger causality  
        at higher frequencies against the  backward Granger causality at lower  
        frequencies. This illustrates that fluctuations in intrinsic connectivity  
        or cortical excitability can induce correlations between forward and  
        backward Granger causality in distinct frequency bounds. This routine  
        will then return unless edited to demonstrate how to simulate timeseries  
        - and how spectral estimators converge on their expected values under  
        the neural mass or dynamic causal model used here.  
          
        See also:  
         spm_ccf2csd.m, spm_ccf2mar, spm_csd2ccf.m, spm_csd2mar.m, spm_mar2csd.m,   
         spm_csd2coh.m, spm_ccf2gew, spm_dcm_mtf.m, spm_Q.m, spm_mar.m and   
         spm_mar_spectral.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/spm_dcm_Granger_asymmetry_demo.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_Granger_asymmetry_demo", *args, **kwargs, nargout=0)
