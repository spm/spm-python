from spm.__wrapper__ import Runtime


def DEMO_AI_NLSI(*args, **kwargs):
    """
      Demo of active inference for trust games  
       __________________________________________________________________________  
         
        This routine uses a Markov decision process formulation of active  
         
        see also: DEM_demo_MDP_habits.m and spm_MPD_VB_X.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/DEMO_AI_NLSI.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("DEMO_AI_NLSI", *args, **kwargs)
