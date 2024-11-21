from spm.__wrapper__ import Runtime


def bf_wizard_features(*args, **kwargs):
    """
      A handy command-line based batch filler with some defaults for DAiSS  
        features module, pick a few options, and it will default for unpopulated  
        fields  
         
        FORMAT [BF, batch, features] = bf_wizard_data(S)  
          S               - input structure  
         
        Output:  
         BF               - Resultant DAiSS BF structure  
         batch            - matlabbatch job for spm_jobman to run  
         features         - simplified summary of options selected  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_wizard_features.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bf_wizard_features", *args, **kwargs)
