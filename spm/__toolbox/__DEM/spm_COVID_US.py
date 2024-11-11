from spm.__wrapper__ import Runtime


def spm_COVID_US(*args, **kwargs):
    """
      Generate predictions and hidden states of a multi-region COVID model  
        FORMAT [Y,X] = spm_COVID_US(P,M,U)  
        P   - model parameters  
        M   - model structure (requires M.T - length of timeseries)  
        U   - number of output variables [default: 2] or indices e.g., [4 5]  
         
        Y(:,1) - number of new deaths  
        Y(:,2) - number of new cases  
        Y(:,3) - CCU bed occupancy  
        Y(:,4) - working days  
        Y(:,5) - herd immunity  
        Y(:,6) - ...  
         
        X{i}    - (M.T x 4) marginal densities over four factors for region i  
        location   : {'home','out','CCU','morgue'};  
        infection  : {'susceptible','infected','infectious','immune'};  
        clinical   : {'asymptomatic','symptoms','ARDS','deceased'};  
        diagnostic : {'untested','waiting','positive','negative'}  
         
        This function returns data Y and their latent states or causes X, given  
        the parameters of a generative model. This model is a mean field  
        approximation based upon population or density dynamics with certain  
        conditional dependencies among the marginal densities over four factors.  
        See SPM_covid_priors details. In brief, this routine transforms model  
        parameters to (exponentiated) scale parameters and then generates a  
        sequence of jointed densities over four factors, after assembling a state  
        dependent probability transition matrix. The number in the timeseries is  
        specified by M.T.  
         
        Equipped with a time-dependent ensemble density, outcome measures are  
        then generated as expected values. These include the rate of (new) deaths  
        and cases per day. This routine can be extended to generate other  
        outcomes, or indeed consider other factorisations of the probability  
        transition matrices. The subroutine (spm_COVID_B) creating the  
        probability transition matrices given the current states and model  
        parameters defines the generative model. This model structure rests upon  
        a mean field approximation to the transition probabilities that,  
        crucially, depends upon (usually the marginal) densities in question.  
        Working through the code below will show how this model is constructed.  
         
        A more detailed description of the generative model can be found in the  
        body of spm_COVID_gen.  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_COVID_US.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_COVID_US", *args, **kwargs)
