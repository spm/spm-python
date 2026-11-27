from spm._runtime import Runtime


def spm_MDP_checkX(*args, **kwargs):
    r"""
      MDP structure checking for XXX routines  
        FORMAT [MDP] = spm_MDP_checkX(MDP,)  
         
        MDP.U(1,F)            - indices of controllable paths  
        MDP.T                 - number of outcomes  
         
        MDP.A{g}(No(g),Ns(1),Ns(2),...)   - likelihood of outcomes given hidden states  
        MDP.B{f}(Ns(f),Ns(f),Nu(f))       - transitions among hidden under MF control states  
        MDP.C{g}(No(g),1)      - prior preferences over outcomes in modality g  
        MDP.D{f}(Ns(f),1)      - prior probabilities over initial states  
        MDP.E{f}(Nu(f),1)      - prior probabilities over initial paths  
        MDP.H{f}(Ns(f),1)      - prior probabilities over final sates  
         
        MDP.a{g}              - concentration parameters for A  
        MDP.b{f}              - concentration parameters for B  
        MDP.c{g}              - concentration parameters for C  
        MDP.d{f}              - concentration parameters for D  
        MDP.e{f}              - concentration parameters for E  
        MDP.h{f}              - concentration parameters for H  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_MDP_checkX.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_MDP_checkX", *args, **kwargs)
