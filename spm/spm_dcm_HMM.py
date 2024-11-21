from spm.__wrapper__ import Runtime


def spm_dcm_HMM(*args, **kwargs):
    """
      PEB Inversion of a DCM under a hidden Markov model of state transitions  
        FORMAT [HMM,CSD] = spm_dcm_HMM(DCM,N,b)  
        FORMAT [HMM]     = spm_dcm_HMM(CSD,b)  
        -------------------------------------------------------------------------  
        DCM{p} - DCMs for p sessons: DCM.b encodes state-dependent connections  
        N      - number of windows within which to evaluate states  
        b{s}   - Cell array state transition priors (Dirichlet parameters)   
         
        returns HMM(s):  
            HMM(s).X  - posterior expectation of hidden states  
            HMM(s).qB - posterior expectation of HMM parameters  
            HMM(s).qb - and Dirichlet concentration parameters  
            HMM(s).qP - posterior expectation of PEB parameters  
            HMM(s).qC - posterior covariances of PEB parameters  
            HMM(s).iP - indices of DCM parameters  
            HMM(s).Ep - posterior expectation of DCM parameters  
            HMM(s).Cp - posterior covariances of DCM parameters  
            HMM(s).L  - free energy components  
            HMM(s).F  - total free energy (model evidence)  
        s  -  index of HMM structure (prior model of state transitions)  
         
        CSD{N,P} - inverted DCM of each window; with window functions in CSD{n}.W  
       __________________________________________________________________________  
         
         This routine characterises a single timeseries in terms of latent or  
         hidden  brain states manifest in terms of state dependent connectivity.  
         It first inverts  the complex cross spectral density of the observed  
         timeseries and  then estimates epoch specific fluctuations in state  
         dependent connectivity in a subset of connections (specified in the  
         logical field DCM.b). The ensuing  sequence of posterior densities are  
         then subject to Bayesian model reduction to provide evidence for  
         sequences of state transitions under a hidden Markov model. Effectively,  
         this involves supplying the evidence that the brain is in a particular  
         connectivity state at each epoch - using the reduced free energy -  to a  
         variational message passing scheme based upon a Markov decision process.  
         The higher (discrete state space for hidden Markov model) level that  
         returns the Bayesian model average for iterative optimisation of the  
         state dependent connection (PEB) parameters, and the epoch specific  
         connectivity (DCM) parameters. The products of this inversion are  
         posteriors at the DCM (epoch specific), PEB, (state specific)and HMM  
         (transition) level. These  posterior densities fully characterise a  
         given time series in terms of discrete  state transitions, where each  
         brain state is associated with a location in (connectivity) parameter  
         space; in other words, a discrete characterisation of dynamic or  
         fluctuating effective connectivity.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_HMM.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_HMM", *args, **kwargs)
