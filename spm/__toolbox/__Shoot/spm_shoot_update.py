from spm.__wrapper__ import Runtime


def spm_shoot_update(*args, **kwargs):
    """
      Shooting Of Diffeomorphisms (Spawn Of Dartel)  
        FORMAT u0 = spm_shoot_update(g,f,u0,phi,dt,prm, bs_args)  
        g        - template  
        f        - individual  
        u0       - initial velocity  
        phi      - deformation  
        dt       - Jacobian determinants  
        prm      - Parameters of differential operator  
        bs_args  - interpolation settings  
        scale    - scaling of the update step  
         
        u0       - updated initial velocity  
        ll1      - matching part of objective function  
        ll2      - regularisation part of objective function  
         
        The easiest way to figure out what this function does is to read the code.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Shoot/spm_shoot_update.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_shoot_update", *args, **kwargs)
