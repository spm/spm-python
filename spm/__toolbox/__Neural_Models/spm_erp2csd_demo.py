from spm.__wrapper__ import Runtime


def spm_erp2csd_demo(*args, **kwargs):
    """
      Demo routine for local field potential models  
       ==========================================================================  
         
        This routine illustrates the use of empirical Bayes, for dynamic causal  
        modelling, in identifying the causes of paroxysmal seizure activity; as  
        expressed in terms of spectral density responses. We first simulate data  
        by generating (endogenous neuronal) inputs under a scale free or power  
        law assumption (the priors used for DCM for CSD). The inputs are used to  
        generate responses over two seconds, whose spectral density is then used  
        to estimate the neural mass model parameters. This is repeated for  
        several different values of a particular intrinsic connection strength.  
        Empirical Bayes is then used to compare competing models of between  
        epoch changes in intrinsic connections. The  posterior distributions  
        are then compared with the true values, under the selected model.  
         
        The key aspects of this demonstration are to show that cross spectral  
        density data features can be used to summarise evoked responses - and  
        that trial to trial (or condition to condition) variations in model  
        parameters can be identified using model selection, under a parametric  
        random effect or empirical Bayesian model, which furnishes posterior  
        densities over parameters at the first or within trial Level.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/spm_erp2csd_demo.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_erp2csd_demo", *args, **kwargs, nargout=0)
