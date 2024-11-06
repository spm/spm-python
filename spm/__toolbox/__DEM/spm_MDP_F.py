from spm.__wrapper__ import Runtime


def spm_MDP_F(*args, **kwargs):
    """
      auxiliary function for retrieving free energy and its components  
        FORMAT [F,Fu,Fs,Fq,Fg,Fa] = spm_MDP_F(MDP)  
         
        F   - total free energy  
        Fu  - confidence  
        Fs  - free energy of states  
        Fq  - free energy of policies  
        Fg  - free energy of precision  
        Fa  - free energy of parameters  
         
        If MDP is a cell array, the free actions are turned (summed over time),  
        otherwise, the free energies are turned over time  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_MDP_F.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_MDP_F", *args, **kwargs)
