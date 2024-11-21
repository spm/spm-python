from spm.__wrapper__ import Runtime


def DEMO_MDP_Stroop(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEMO_MDP_Stroop.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEMO_MDP_Stroop", *args, **kwargs)
