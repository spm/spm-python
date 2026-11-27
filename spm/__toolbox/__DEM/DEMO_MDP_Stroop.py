from spm._runtime import Runtime


def DEMO_MDP_Stroop(*args, **kwargs):
    r"""
      This demo uses a deep temporal partially observed Markov decision  
        process to simulate performance of a Stroop task. This task is used to  
        illustrate a formulation of cognitive or mental effort. The synthetic  
        participants must overcome a prior belief that the normal action on  
        being presented with text is to read that word, and instead state the  
        colour the text is presented in. In addition, this routine demonstrates  
        the fitting of choice and reaction time data to the model, and the  
        recovery of parameters that summarise behaviour.  
          
        see also: spm_MDP_VB_X.m, DEM_demo_MDP_reading.m, DEMO_MDP_questions.m  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEMO_MDP_Stroop.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEMO_MDP_Stroop", *args, **kwargs)
