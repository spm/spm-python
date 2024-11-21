from spm.__wrapper__ import Runtime


def spm_COVID_priors_R(*args, **kwargs):
    """
      Prior expectation and covariance of between region parameters  
        FORMAT [pE,pC,str,erc] = spm_COVID_priors_R(data)  
          
        data(N)     - Meta data, including distance between regions  
          
        pE          - prior expectation (structure)  
        pC          - prior covariances (structure)  
        str.names   - parameter names  
        str.regions - regional names  
         
        This routine assembles the (Gaussian) and priors over the parameters of a  
        generative model for COVID-19. This generative model is based upon a mean  
        field approximation to ensemble of population dynamics, in which four  
        marginal distributions are coupled through probability transition  
        matrices. The marginal distributions correspond to 4 factors;  
        namely,location, infection, clinical and diagnostic or testing states.  
        Please see spm_COVID_priors for details. This routine prepares the priors  
        for the parameters that couple different regions (e.g., American states).  
        These parameters include the (effective) connectivity that controls the  
        flux of people from one region to another. The total population size in  
        these models is included as a precise prior, while the number of initial  
        cases is allowed to vary to accommodate differential onset times.  
        Finally, there is a federal parameter that determines the balance between  
        region specific and federal densities in mediating lockdown or social  
        distancing strategies.  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_COVID_priors_R.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_COVID_priors_R", *args, **kwargs)
