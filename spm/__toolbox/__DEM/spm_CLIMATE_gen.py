from spm.__wrapper__ import Runtime


def spm_CLIMATE_gen(*args, **kwargs):
    """
      Generate predictions and hidden states of a CLIMATE model  
        FORMAT [Y,X,T] = spm_CLIMATE_gen(P,M,U,NPI)  
        P    - model parameters  
        M    - model structure (M.T - dates or data structure with dates)  
        U    - indices of output variables to generate  
        NPI  - intervention  
            NPI(i).period = {'dd-mm-yyyy','dd-mm-yyyy'}; % dates to evaluate  
            NPI(i).param  = {'xyz',...};                 % parameter name  
            NPI(i).Q      = (value1,...);                % parameter value  
            NPI(i).dates  = {'dd-mm-yyyy','dd-mm-yyyy'}; % dates of interevention  
         
        Y: (output variables)  
            'Average temperature';  
            'Extreme drought';  
            'Exceptional drought';  
            'Rainfall';  
            'Crop production';  
            'Irrigation';  
            'Fertiliser use';  
            'Milk production';  
            'Food prices';  
            'Economic activity';  
            'Income in exposed sector';  
            'Childhood malnutrition';  
            'Crop yield';  
         
        X: (latent states)  
             Meteorological (fast)  
             Meteorological (fast)  
             Meteorological (slow)  
             Anthropological activity  
             Primary sector activity  
             Yield  
             Crop production  
             Irrigation  
             Crop resources (fertilisation)  
             Food production  
             Food price  
             Malnutrition  
         
        This function returns outcomes Y and their latent states or causes X,  
        given the parameters of a generative model P. Generative models of this  
        (state space) sort have two parts. The first part concerns fluctuations  
        in latent states specified in terms of equations of motion (technically,  
        ordinary differential equations). The second part concerns the mapping  
        from the latent states to the observable outcomes. This means the  
        parameters of the generative model can be divided into the parameters of  
        the equations of motion (e.g., rate or time constants) and the parameters  
        of the likelihood mapping. In this instance, the likelihood mapping is  
        from latent states to log transformed outcomes and is a simple linear  
        mapping – such that the coefficients can be thought of as constants and  
        regression coefficients.  
         
        The parameters of the equations of motion are slightly more complicated  
        and define the system at hand, in terms of which latent states can  
        influence others. Because we want to evaluate the posterior predictive  
        density over future states, we have to specify everything in terms of  
        parameters (in the absence of any outside or endogenous inputs). This  
        means everything has to be specified in terms of (time invariant)  
        parameters, including the initial states at a specified time (d0). This  
        also means that one models different scenarios (e.g., interventions) in  
        terms of changes in parameters over particular time points, that can be  
        specified in an optional argument (NPI).  
         
        This model contains 12 latent states and (by coincidence) 12 outputs. The  
        12 latent states are coupled to each other dynamically through their  
        equations of motion and then generate outcomes as mixtures of one or more  
        latent states. The code below has been annotated to describe the coupling  
        among states (that specifies the dynamical part of the model) and the  
        coupling from states to output (that specifies the observation part of  
        the model).  
         
        For a detailed description of the role of each parameter please see  
        spm_CLIMATE_priors.  
         
        This script contains some auxiliary code (at the end) that allows one to  
        examine the effects of changing various parameters by cutting and pasting  
        the appropriate section. For a more mathematical rendition of the model,  
        the equations of motion – and Jacobian – can be displayed in latex  
        formatby putting a breakpoint in the current file (so that the sub  
        function can be referenced) and then cutting and pasting the appropriate  
        section into the command window.  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_CLIMATE_gen.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_CLIMATE_gen", *args, **kwargs)
