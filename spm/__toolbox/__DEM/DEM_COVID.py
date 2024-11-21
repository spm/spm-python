from spm.__wrapper__ import Runtime


def DEM_COVID(*args, **kwargs):
    """
      FORMAT [DCM,GCM] = DEM_COVID(country,data)  
        data    - data    to model [default: data = DATA_COVID_JHU]  
        country - country to model [default: 'United Kingdom')  
         
        Demonstration of COVID-19 modelling using variational Laplace  
       __________________________________________________________________________  
         
        This routine illustrates the Bayesian model inversion of a generative  
        model of coronavirus spread using variational techniques (variational  
        Laplace). It illustrates hierarchical Bayesian modelling by first  
        inverting a generative model of each country, and then combining the  
        posterior densities over the model parameters using parametric empirical  
        Bayes to leverage systematic differences between countries, as  
        characterised by their population, geographical location etc.  
         
        Each subsection produces one or two figures that are described in the  
        annotated (Matlab) code. These subsections core various subroutines that  
        provide a more detailed description of things like the generative model,  
        its priors and the evaluation confidence intervals.  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_COVID.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_COVID", *args, **kwargs)
