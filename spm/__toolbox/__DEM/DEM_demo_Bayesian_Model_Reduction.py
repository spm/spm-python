from spm.__wrapper__ import Runtime


def DEM_demo_Bayesian_Model_Reduction(*args, **kwargs):
    """
      This demonstration code illustrates the application of post hoc model   
        optimisation or Bayesian model reduction (BMR) in identifying gene and   
        gene-gene interaction effects in behavioural or physiological variables.    
        The basic idea is to replace conventional heuristics based on the   
        assumption that the contribution of any gene is sampled from a sparse   
        distribution (such that a small number contribute and a large number do   
        not) with an explicit search over a model space that includes all sparse  
        and non-sparse models.  This exhaustive search rests upon recent   
        advances in model optimisation based upon variational Bayesian model   
        inversion.  In short, it is possible to estimate the posterior   
        distribution of model parameters under a reduced model, given the   
        posterior and prior distributions under a full model.    
        In this context, a reduced model corresponds to a model in which some   
        parameters are removed (by shrinking their prior variance to zero).    
        This means that it is only necessary to invert the full model and then   
        perform automatic BMR (over all possible combinations of parameters)   
        using a greedy search based upon the free energy approximation to log   
        model evidence.  With sufficient signal to noise, this scheme can   
        recover the small number of effects, even in under determined or   
        ill-posed problems (where the number of potential effects can vastly   
        exceed the number of samples).   
         
        The illustration below uses 128 subjects who have been measured three   
        times (say in three brain regions) and we want to model these   
        measurements in terms of first and second order genetic contributions   
        given 8 (binary) genetic variables and all (unique) pair wise   
        interactions.  This means that there are 36 unknown parameters   
        (excluding a constant and, say, age confounds over subjects).  In the   
        scheme below, each measurement is inverted separately under a simple   
        (polynomial) model with uninformative priors on the parameters and   
        (precision) hyper-parameters describing beliefs about signal to noise.    
        A fixed effects Bayesian model averaging (BMA) scheme is used in   
        combination with BMR to identify the best model out of all possible   
        combinations of first and second order effects.  With the signal to   
        noise and number of samples used in this simulation, the recovery is   
        generally perfect.  This scheme also illustrates inference over a   
        partition of model space (or families of models).  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_demo_Bayesian_Model_Reduction.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_demo_Bayesian_Model_Reduction", *args, **kwargs)
