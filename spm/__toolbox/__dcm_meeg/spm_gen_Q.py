from spm.__wrapper__ import Runtime


def spm_gen_Q(*args, **kwargs):
    """
      Helper routine for spm_gen routines  
        FORMAT [Q] = spm_gen_Q(P,X)  
         
        P - parameters  
        X - vector of between trial effects  
        c - trial in question  
         
        Q - trial or condition-specific parameters  
         
        This routine computes the parameters of a DCM for a given trial, where  
        trial-specific effects are deployed according to a design vector X. The  
        parameterisation follows a standard naming protocol where, for example,  
        X(1)*P.B{1} + X(2)*P.B{2}... adjusts P.A for all (input) effects encoded  
        in P.B.  
        P.BN and P.AN operate at NMDA receptors along extrinsic connections  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_gen_Q.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_gen_Q", *args, **kwargs)
