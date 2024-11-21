from spm.__wrapper__ import Runtime


def spm_ekf(*args, **kwargs):
    """
      Extended Kalman Filtering for dynamic models  
        FORMAT [x,P] = spm_ekf(M,y)  
        M - model specification structure  
        y - output or data (N x T)  
         
        M(1).x                            % initial states  
        M(1).f  = inline(f,'x','v','P')   % state equation  
        M(1).g  = inline(g,'x','v','P')   % observer equation  
        M(1).pE                           % parameters  
        M(1).V                            % observation noise precision  
         
        M(2).v                            % initial process f(noise)  
        M(2).V                            % process f(noise) precision  
         
        x - conditional expectation of states  
        P - {1 x T} conditional covariance of states  
       __________________________________________________________________________  
        See notes at the end of this script for details and a demo.  This routine  
        is based on:  
         
        var der Merwe R, Doucet A, de Freitas N and Wan E (2000). The  
        unscented particle filter.  Technical Report CUED/F-INFENG/TR 380  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_ekf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_ekf", *args, **kwargs)
