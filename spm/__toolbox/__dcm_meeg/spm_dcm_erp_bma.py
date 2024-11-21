from spm.__wrapper__ import Runtime


def spm_dcm_erp_bma(*args, **kwargs):
    """
      Compute posterior over connections, or modulatory gains in them, from BMA  
        FORMAT [r,xp] = spm_dcm_erp_bma (BMS_file,stats,params)  
         
        BMS_file      Name of Bayesian Model Selection .mat file  
        stats         'ffx' or 'rfx'   
        params        Parameter data structure  
                      .type          'A' (connection) or 'B' (gain in connection)  
                      .hier          'forward', 'backward' or 'lateral' (for conn_type='A')  
                      .ip            eg 1, 2, 3 indexes modulatory input (for conn_type='B')  
                      .to            to region eg 3  
                      .from          from region eg 1  
                      .xt            exceedance threshold (typically set to 1)  
                      .C             [nr x nr] contrast matrix where nr is the number of regions   
         
         
        r             posterior samples  
        xp            exceedance probability  
                      This is the posterior probability that the connection is  
                      larger than params.xt. Alternatively, if you are looking at  
                      a contrast of connections, its the posterior probability  
                      that the contrast is greater than zero.  
         
        The parameters returned by Bayesian Model Averaging (BMA) are the 'latent'  
        variables A and B which are Gaussian (and consequently can be positive or  
        negative).    
         
        The corresponding connection strengths (rA) or gains in connection  
        strength (rB) are an exponential function of these latent variables.   
        These are the values we are interested in and want to make an inference  
        about.  
         
        This routine computes the posterior distribution over rA or rB by  
        generating samples from the latent variables, and exponentiating each  
        sample.   
         
        The probability that the rA or RB values are greater than some threshold  
        xt (such as unity) is then just the proportion of posterior samples that  
        are greater than xt.  
         
        If a contrast matrix (C) is not specifed this function looks at a single  
        connection or gain. To look at relative sizes of connection/gain values   
        enter a C matrix. eg. to test, in a 3 region DCM, is connection from 3  
        to 2 bigger than 2 to 3 ? set C=[0 0 0; 0 0 1; 0 -1 0].  
         
       --------------------------------------------------------------------------  
          
        Example usage:   
         
        1. Look at a single connection value:  
         
        params.type='A'; params.hier='forward';   
        params.to=3; params.from=1; params.xt=1;  
        spm_dcm_erp_bma([],'ffx',params);  
         
        2. Look at a single gain value:  
         
        params.type='B'; params.ip=1;   
        params.to=1; params.from=1; params.xt=1;  
        spm_dcm_erp_bma([],'ffx',params);  
         
        3. Look at a contrast of connection values:  
         
        params.type='B'; params.ip=1;  
        params.C=[0 0 0; 0 0 1; 0 -1 0];  
        spm_dcm_erp_bma([],'ffx',params);  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_dcm_erp_bma.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_erp_bma", *args, **kwargs)
