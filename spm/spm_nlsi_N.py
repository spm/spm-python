from spm.__wrapper__ import Runtime


def spm_nlsi_N(*args, **kwargs):
    """
      Bayesian inversion of a linear-nonlinear model of the form F(p)*G(g)'  
        FORMAT [Ep,Eg,Cp,Cg,S,F,L]= spm_nlsi_N(M,U,Y)  
         
        Generative model  
       __________________________________________________________________________  
          
        M.IS - IS(p,M,U) A prediction generating function name; usually an   
               integration scheme for state-space models of the form  
         
               M.f  - f(x,u,p,M) - state equation:  dxdt = f(x,u)  
         
               that returns hidden states - x; however, it can be any nonlinear  
               function of the inputs u. I.e., x = IS(p,M,U)  
         
        M.G  - G(g,M) - linear observer: y = (x - M.x')*G(g,M)'  
         
        M.FS - function name f(y,M) - feature selection  
               This [optional] function performs feature selection assuming the  
               generalized model y = FS(y,M) = FS(x*G',M) + X0*P0 + e  
         
        M.x  - The expansion point for the states (i.e., the fixed point)  
         
        M.P  - starting estimates for model parameters [ states - optional]  
        M.Q  - starting estimates for model parameters [ observer - optional]  
         
        M.pE - prior expectation  - of model parameters - f(x,u,p,M)  
        M.pC - prior covariance   - of model parameters - f(x,u,p,M)  
         
        M.gE - prior expectation  - of model parameters - G(g,M)  
        M.gC - prior covariance   - of model parameters - G(g,M)  
         
        M.hE - prior expectation  - E{h}   of log-precision parameters  
        M.hC - prior covariance   - Cov{h} of log-precision parameters  
         
        U.u  - inputs  
        U.dt - sampling interval  
         
        Y.y  - {[ns,nx],...} - [ns] samples x [nx] channels x {trials}  
        Y.X0 - Confounds or null space  
        Y.dt - sampling interval for outputs  
        Y.Q  - error precision components  
         
         
        Parameter estimates  
       --------------------------------------------------------------------------  
        Ep  - (p x 1)         conditional expectation  E{p|y}  
        Cp  - (p x p)         conditional covariance   Cov{p|y}  
         
        Eg  - (p x 1)         conditional expectation  E{g|y}  
        Cg  - (p x p)         conditional covariance   Cov{g|y}  
         
        S   - (v x v)         [Re]ML estimate of error Cov{e(h)}  
         
        log evidence  
       --------------------------------------------------------------------------  
        F   - [-ve] free energy F = log evidence = p(y|m)  
          
            L(1) = - ey'*iS*ey/2;             accuracy of states  
            L(2) = - ep'*ipC*ep/2;            accuracy of parameters (f)  
            L(3) = - eg'*igC*eg/2;            accuracy of parameters (g)  
            L(4) = - eu'*iuC*eu/2;            accuracy of parameters (u)  
            L(5) = - eh'*ihC*eh/2;            accuracy of precisions (u)  
            L(6) = - ns*nr*log(8*atan(1))/2;  constant  
            L(7) = - nq*spm_logdet(S)/2;      precision  
            L(8) = spm_logdet(ibC*Cb)/2;      parameter complexity  
            L(9) = spm_logdet(ihC*Ch)/2;      precision complexity  
         
       __________________________________________________________________________  
        Returns the moments of the posterior p.d.f. of the parameters of a  
        nonlinear model specified by IS(P,M,U) under Gaussian assumptions. Usually,  
        IS would be an integrator of a dynamic MIMO input-state-output model   
         
                     dx/dt = f(x,u,p)  
                     y     = G(g)*x  + X0*B + e  
         
        The E-Step uses a Fisher-Scoring scheme and a Laplace  
        approximation to estimate the conditional expectation and covariance of P  
        If the free-energy starts to increase, a Levenberg-Marquardt scheme is  
        invoked.  The M-Step estimates the precision components of e, in terms  
        of [Re]ML point estimators of the log-precisions.  
        An optional feature selection can be specified with parameters M.FS  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_nlsi_N.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_nlsi_N", *args, **kwargs)
