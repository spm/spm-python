from spm.__wrapper__ import Runtime


def DEM_COVID_DASH(*args, **kwargs):
    """
      FORMAT [DCM] = DEM_COVID_DASH  
         
        Demonstration of COVID-19 modelling using variational Laplace  
       __________________________________________________________________________  
         
        The estimates of the reproduction rate and associated prevalence of  
        infection in each region are based on a dynamic causal model of the  
        coronavirus outbreak. This kind of modelling is distinct from  
        conventional epidemiological modelling because the dynamic causal model  
        incorporates things like self-isolation, social distancing, the  
        probability of being tested and waiting for test results. This allows us  
        to use regional reports of COVID-19 related deaths and new cases to model  
        regional outbreaks.  
          
        In brief, the model assumes each region experiences an epidemic with  
        similar characteristics but with different parameters, such as the number  
        of contacts at home or work. And different mixtures of people who are  
        more or less likely to catch (or transmit) the virus. These parameters  
        are estimated from regional data and are then used to nowcast and  
        forecast the evolution of the outbreak in terms of underlying or latent  
        causes (such as the prevalence of infection). The effective population  
        size is the number of people who are caught up in the outbreak, some of  
        whom will be resistant to catching the virus. Of those that are not, some  
        will become contagious and infect other people. From these estimates it  
        is possible to evaluate the effective reproduction ratio at any point in  
        time during the course of the outbreak, in addition to other quantitative  
        estimates, such as the number of people currently infected or new cases  
        of infection every day (that may or may not be identified).  
          
        The ensuing predictions complement equivalent estimates from  
        epidemiological modelling based upon the history of outcomes observed so  
        far. See https://www.mrc-bsu.cam.ac.uk/now-casting/ for a  
        state-of-the-art transmission model. In principle, it is possible to  
        compare the quality of dynamic causal and epidemiological models in terms  
        of their model evidence or marginal likelihood. However, at the present  
        time, it is difficult to estimate the evidence for epidemiological  
        models; thereby precluding (Bayesian) model comparison.  
          
        Technical details about the dynamic causal model used here can be found  
        at https://www.fil.ion.ucl.ac.uk/spm/covid-19/.  
          
        The (annotated) open source code creating these graphics is  
        DEM_COVID_DASH.m  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_COVID_DASH.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_COVID_DASH", *args, **kwargs)
