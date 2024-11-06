from spm.__wrapper__ import Runtime


def DEMO_model_reduction_ERP(*args, **kwargs):
    """
      Illustration of (post hoc) neuronal mass model optimisation  
       __________________________________________________________________________  
        This demonstration routine illustrates the post-hoc optimisation of  
        dynamic causal models for event related responses. To assess performance  
        in relation to ground truth, it uses simulated data. We will simulate a  
        simple two source model with exogenous input to the first source and  
        reciprocal (extrinsic) connections between the two sources. the ERPs are  
        simulated and two conditions, where the second condition induces a change  
        in the intrinsic coupling of the first source and the forward extrinsic  
        coupling. We then explore a simple model space; created by increasing the  
        precision of shrinkage priors on the intrinsic condition specific effect.  
        Because this effect was responsible for generating the data, we expect  
        the free energy (log evidence) to fall as the shrinkage covariance falls  
        to 0). Crucially, we compare and contrast the estimates of the free  
        energy (and parameter estimates) using an explicit inversion of the  
        reduced models (with tighter shrinkage priors) and a post-hoc model  
        reduction procedure - that is computationally more efficient and  
        robust to local minima.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/DEMO_model_reduction_ERP.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEMO_model_reduction_ERP", *args, **kwargs, nargout=0)
