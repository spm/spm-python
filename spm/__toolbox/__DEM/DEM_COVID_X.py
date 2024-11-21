from spm.__wrapper__ import Runtime


def DEM_COVID_X(*args, **kwargs):
    """
      FORMAT [DCM] = DEM_COVID_X(Y,data)  
        data    - data to model [default: data = DATA_COVID_US]  
         
        Demonstration of COVID-19 modelling using variational Laplace  
       __________________________________________________________________________  
         
        This routine illustrates the Bayesian model inversion of a generative  
        model of coronavirus spread using variational techniques (variational  
        Laplace). This (pandemic) model is composed of regional (epidemic)  
        models. In brief, the model for a single region comprises four factors,  
        each with four states, giving 256 states or compartments per region.  
        These regional models are then assembled to model the coupling among  
        eight regions giving 256^8 compartments. However, due to certain  
        conditional independencies, this can be treated as a collection of 256  
        compartmental models; providing one carefully links the state of one  
        region to the state of another. Here, this linking or connectivity is  
        parameterised in terms of a probability flux or exchange of people from  
        one regional population to another. Regional factors include location,  
        immune status, clinical status and testing status. The transitions among  
        states of any factor depends upon other factors. For example, the  
        probability that I will move from a state of being asymptomatic to being  
        symptomatic depends upon whether I am infected or not. Similarly, the  
        probability that I will move from one region to another depends upon  
        whether I am at work (i.e., not at home). In short, the exchange between  
        different regional populations is limited to the people who are not at  
        home and are consequently in a position to travel. The parameters of  
        interregional coupling correspond to rate constants or effective  
        connectivity that can be reciprocal and asymmetric. For example, the  
        probability of moving to New York from New Jersey does not have to be the  
        same as a probability of moving from New Jersey to New York. Note that  
        the movement between regions can be restricted to a chain. In other  
        words, to get from the first state to the last state, I have to go  
        through all other states.  
         
        Each subsection produces one or two figures that are described in the  
        annotated (Matlab) code. These subsections call various subroutines that  
        provide a more detailed description of things like the generative model,  
        its priors and the evaluation of confidence intervals.  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEM_COVID_X.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEM_COVID_X", *args, **kwargs)
