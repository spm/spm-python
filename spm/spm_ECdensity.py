from spm._runtime import Runtime


def spm_ECdensity(*args, **kwargs):
    r"""
      Return the Euler characteristic (EC) density  
        FORMAT function [EC] = spm_ECdensity(STAT,t,df)  
       __________________________________________________________________________  
         
        Reference : Worsley KJ et al (1996), Hum Brain Mapp. 4:58-73  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_ECdensity.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_ECdensity", *args, **kwargs)
