from spm.__wrapper__ import Runtime


def _randomseed(*args, **kwargs):
    """
      RANDOMSEED retrieves or sets the random seed, taking into account the different  
        MATLAB version specific methods  
         
        Use as  
          state = randomseed(setseed)  
         
        INPUT  
        setseed    []              does not reset the state, but saves out the state for future use  
                   integer         seed value to set to specific state  
                   state vector    state value (vector) output from previous call to setting the state  
         
        OUTPUT  
        state      vector of current state (or seed only)  
         
        The output can be used as input re-create the same random number sequence  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/randomseed.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("randomseed", *args, **kwargs)
