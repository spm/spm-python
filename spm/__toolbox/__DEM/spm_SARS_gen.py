from spm.__wrapper__ import Runtime


def spm_SARS_gen(*args, **kwargs):
    """
      Generate predictions and hidden states of a COVID model  
        FORMAT [Y,X,Z,W] = spm_SARS_gen(P,M,U,NPI,age)  
        P    - model parameters  
        M    - model structure (M.T - length of timeseries or data structure)  
        U    - number of output variables [default: 2] or indices e.g., [4 5]  
        NPI  - nonpharmaceutical intervention  
            NPI(i).period = {'dd-mm-yyyy','dd-mm-yyyy'}; % dates of epidemic  
            NPI(i).param  = {'xyz',...};                 % parameter name  
            NPI(i).Q      = (value1,...);                % parameter name  
            NPI(i).dates  = {'dd-mm-yyyy','dd-mm-yyyy'}; % dates of interevention  
        age  - indices of age band (0 for average)  
         
        Y(:,1)  - Daily deaths (28 days)  
        Y(:,2)  - Daily confirmed cases  
        Y(:,3)  - Mechanical ventilation  
        Y(:,4)  - Reproduction ratio (R)  
        Y(:,5)  - Seroprevalence {%}  
        Y(:,6)  - testing rate (PCR and LFD)  
        Y(:,7)  - Risk of infection (%)  
        Y(:,8)  - Prevalence (true) {%}  
        Y(:,9)  - Daily contacts  
        Y(:,10) - Daily incidence (%)  
        Y(:,11) - Prevalence (positivity){%}  
        Y(:,12) - Number symptomatic  
        Y(:,13) - Mobility (%)  
        Y(:,14) - Workplace (%)  
        Y(:,15) - Certified deaths  
        Y(:,16) - Hospital admissions  
        Y(:,17) - Hospital deaths  
        Y(:,18) - Non-hospital deaths  
        Y(:,19) - Daily incidence (per hundred thousand)  
        Y(:,20) - Weekly confirmed cases (per hundred thousand)  
        Y(:,21) - Infection fatality ratio (%)  
        Y(:,22) - Cumulative first dose  
        Y(:,23) - PCR case positivity (%)  
        Y(:,24) - Lateral flow tests  
        Y(:,25) - Cumulative attack rate  
        Y(:,26) - Population immunity (total)  
        Y(:,27) - Hospital cases  
        Y(:,28) - Incidence of Long Covid  
        Y(:,29) - Vaccine immunity (seropositive)  
        Y(:,30) - Cumulative admissions  
        Y(:,31) - Vaccine effectiveness (prevalence)  
        Y(:,32) - Gross domestic product  
        Y(:,33) - Doubling time  
        Y(:,34) - Incidence of new cases (total)  
        Y(:,35) - Serial interval (days)  
        Y(:,36) - Cumulative vaccines (M)  
         
        X       - (M.T x 4) marginal densities over four factors  
        location   : {'home','out','ccu','removed','isolated','hospital'};  
        infection  : {'susceptible','infected','infectious','Ab +ve','Ab -ve','vaccine +ve','infected (vac)','infectious (vac)'};  
        clinical   : {'asymptomatic','symptoms','ARDS','death'};  
        diagnostic : {'untested','waiting','PCR +ve','PCR -ve','LFD +ve','LFD -ve'}  
         
        Z{t} - joint density over hidden states at the time t  
        W    - structure containing time varying parameters  
         
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
        transition matrices. The subroutine (spm_COVID_T) creating the  
        probability transition matrices given the current states and model  
        parameters defines the generative model. This model structure rests upon  
        a mean field approximation to the transition probabilities that,  
        crucially, depends upon (usually the marginal) densities in question.  
        Working through the code below will show how this model is constructed.  
         
        A more detailed description of the generative model can be found in the  
        body of the script.  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_SARS_gen.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_SARS_gen", *args, **kwargs)
