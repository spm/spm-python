from spm.__wrapper__ import Runtime


def spm_ECdensity(*args, **kwargs):
    """
      Return the Euler characteristic (EC) density  
        FORMAT function [EC] = spm_ECdensity(STAT,t,df)  
       __________________________________________________________________________  
         
        Reference : Worsley KJ et al (1996), Hum Brain Mapp. 4:58-73  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_ECdensity.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_ECdensity", *args, **kwargs)
