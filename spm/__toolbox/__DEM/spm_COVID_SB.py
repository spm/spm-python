from spm._runtime import Runtime


def spm_COVID_SB(*args, **kwargs):
    """
      state dependent probability transition matrices  
        FORMAT T = spm_COVID_SB(P,I,dim,Prev,Pcco,Pinh,Pinw)  
        P      - model parameters  
          
        T      - probability transition matrix  
         
        This subroutine creates a transition probability tensors as a function of  
        model parameters and the joint density over four factors, each with  
        several levels. Crucially the transition probabilities of any one factor  
        depend only upon another factor. for example, in the factor modelling  
        clinical status, the transition from acute respiratory distress (ARDS) to  
        death depends upon infection status (infected or not infected) and  
        location (in a critical care unit or not). This version has no absorbing  
        states. States such as contributing to daily deaths or tests are modelled  
        by remaining in that state for one day and then returning to another  
        state.  
       __________________________________________________________________________  
        Copyright (C) 2020 Wellcome Centre for Human Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_COVID_SB.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_COVID_SB", *args, **kwargs)
