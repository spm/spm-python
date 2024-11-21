from spm.__wrapper__ import Runtime


def _nex_info(*args, **kwargs):
    """
      nex_info(filename) -- read and display .nex file info  
         
        [nvar, names, types] = nex_info(filename)  
         
        INPUT:  
          filename - if empty string, will use File Open dialog  
        OUTPUT:  
          nvar - number of variables in the file  
          names - [nvar 64] array of variable names  
          types - [1 nvar] array of variable types  
                  Interpretation of type values: 0-neuron, 1-event, 2-interval, 3-waveform,   
                               4-population vector, 5-continuous variable, 6 - marker  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/nex_info.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("nex_info", *args, **kwargs)
