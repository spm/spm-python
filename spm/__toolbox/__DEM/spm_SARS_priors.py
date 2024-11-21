from spm.__wrapper__ import Runtime


def spm_SARS_priors(*args, **kwargs):
    """
      Generate prior expectation and covariance log parameters  
        FORMAT [pE,pC,str,rfx] = spm_SARS_priors(nN)  
         
        nN          - number of age groups  
         
        pE          - prior expectation (structure)  
        pC          - prior covariances (structure)  
        str.factor  - latent or hidden factors  
        str.factors - levels of each factor  
        str.outcome - outcome names (see spm_SARS_gen)  
        str.names   - parameter names  
        str.field   - field names of random effects  
        rfx         - indices of random effects  
         
        This routine assembles the (Gaussian) and priors over the parameters of a  
        generative model for SARS-19. This generative model is based upon a mean  
        field approximation to ensemble of population dynamics, in which four  
        marginal distributions are coupled through probability transition  
        matrices. The marginal distributions correspond to 4 factors; namely,  
        location, infection, symptom and testing (LIST) states. The parameters of  
        this model determine the initial (probability) states and the transitions  
        among the states that show certain conditional independences.  
         
        These parameters can either be interpreted in terms of the probability of  
        moving from one state to another of a given factor, conditioned on  
        another. Alternatively, in some instances (specifically, staying in the  
        same state),the parameters can be thought of as log transformed rate  
        constants or inverse time constants.  
         
        All the parameters of this generative model are log scale parameters. In  
        other words, the parameters are non-negative but are  encoded in terms of  
        their logarithms. This means that priors over parameters can be specified  
        in terms of a prior expectation and covariance and Gaussian assumptions  
        (i.e., lognormal priors over scale parameters).  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_SARS_priors.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_SARS_priors", *args, **kwargs)
