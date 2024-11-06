from spm.__wrapper__ import Runtime


def DEM_CLIMATE_India(*args, **kwargs):
    """
      FORMAT DCM = DEM_CLIMATE_India  
         
        Demonstration of climate and sustainability modelling  
       __________________________________________________________________________  
         
        This demonstration routine illustrates the use of dynamic causal  
        modelling to test hypotheses about the causal architecture that couples  
        economic activity to meteorological (and climate) variables. This example  
        uses various timeseries from different regions (states) in India  
        quantified in terms of temperature, rainfall, drought, irrigation,  
        economic activity, measures of malnutrition et cetera.  
         
        The dynamic causal model in this instance is a nonlinear deterministic  
        (mean field) approximation to the expected (i.e., average) evolution of  
        various latent states that generate observable data. Crucially, these  
        data can be sparse and discontinuous in time. This means that the unknown  
        variables of the implicit forward or generative model are the model  
        parameters; namely, the rate or time constants coupling latent  
        (unobservable) states and the parameters of a likelihood mapping from  
        latent states to (observable) outcomes. In other words, because the model  
        is deterministic, the latent states are fully determined by the  
        parameters of the generative model, where these parameters can include  
        the initial states.  
         
        The structure and functional form of the model is described in the  
        annotated routines that generates timeseries from latent states, where  
        the latent states are the solution to ordinary differential equations  
        that describe the influence of one latent state on another. For example,  
        there is a latent state called 'anthropomorphic activity' (c.f.,  
        population size) that drives a slow meteorological variable, which  
        increases the amplitude of annual fluctuations in two (fast)  
        meteorological variables. The meteorological variables determine the  
        natural yield of agricultural activity, which in turn influences the use  
        of irrigation and fertilisers. This influences crop production that  
        contributes to food production and, ultimately, anthropomorphic activity,  
        via a latent state called 'malnutrition'. In short, we have a nonlinear  
        dynamical system in which anthropomorphic activity is coupled directly to  
        meteorological (i.e., climate-like) states that are vicariously coupled  
        back to anthropomorphic states. The implicit separation of timescales  
        within the meteorological states results in itinerant dynamics at a fast  
        (seasonal) and slow (decades) timescale.  
         
        This routine first illustrates the way in which data are assembled and  
        sorted. Here, we average away random fluctuations by averaging over  
        regions and then log transform any non-negative data. This allows one to  
        use a simple likelihood model with additive Gaussian noise. We next  
        assemble the prior density over the parameters and hyperparameters  
        controlling the amplitude of observation noise. finally, we invert the  
        model to estimate the parameters in terms of a posterior density. The  
        posterior density over model parameters can then be used in a variety of  
        ways:  
         
        First, one can ask whether any parameters are redundant. In other words,  
        is the model too expressive or over-parameterised. In the example  
        provided, we ask a slightly subtler question: did this parameter need to  
        be a free parameter or could we have fixed it to its prior expectation.  
        This question can be asked by comparing models with uninformative and  
        very precise shrinkage priors over each parameter or combinations of  
        parameters. The same kind of comparison can also be used to test  
        hypotheses by comparing the log evidence of a model with and without a  
        particular link or parameter. In Bayesian model reduction, different  
        models correspond to different shrinkage priors (i.e., a model with out a  
        particular parameter is specified with priors that shrink it towards a  
        small value).  
         
        The posterior density can also be used to assess the role of different  
        parameters, in generating outcomes, using a straightforward sensitivity  
        analysis. This is based on the change in an outcome produced by a change  
        in the parameter, where the outcome is a function of time. Finally, one  
        can integrate (i.e., solve) the model using the posterior estimates of  
        the model parameters to predict what might happen in the future, under  
        different scenarios or plausible interventions.  
         
        Details about the model structure and assumptions (i.e., priors) can  
        be found in the key routines that return the priors (i.e.,  
        spm_CLIMATE_priors) and the routine that generates predicted outcomes,  
        as a function of the parameters (i.e., spm_CLIMATE_gen). The remaining  
        routines are part of the standard SPM software; including the model  
        inversion or deconvolution scheme which, in this deterministic setting,  
        rests on something called variational Laplace  
         
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_CLIMATE_India.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_CLIMATE_India", *args, **kwargs)
