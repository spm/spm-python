from spm._runtime import Runtime


def spm_NESS_priors(*args, **kwargs):
    r"""
      priors for a NESS genertive model  
        FORMAT [pE,pC] = spm_NESS_priors(n,L,V,[W,J,R,C])  
       --------------------------------------------------------------------------  
        n   - number of states (n)  
        L   - order (+1) of polynomial expansion  
        V   - prior covariance over parameters  
        W   - precisions of random fluctuations  
        J   - contraints on solenoidal parameters [ones(n,n)]  
        R   - contraints on surprisal parameters [zeros(n,n)]  
        C   - covariance of NESS [eye(n,n)]  
         
        pE  - prior expectation  
        pC  - prior covariances  
         
        pE.Qp(nb,n,n)       % polynomial coefficients for solenoidal flow {J}  
        pE.Rp(nb,n)         % polynomial coefficients for surprisal {R}  
        pE.Sp(nb,n,n)       % polynomial coefficients for kernel {C}  
        pE.Gp(n,n)          % polynomial coefficients for fluctuations  
        pE.W(n,n)           % precision of random fluctuations   
          
        This routine returns the prior expectations and covariances of the  
        parameters (i.e., polynomial coefficients) of a nonequilibrium  
        steady-state model. This model is based upon the Helmholtz-Hodge  
        decomposition of the solution to density dynamics of any system that  
        possesses a pullback attractor. The requisite flow operators Q and  
        surprisal S are parameterised to 1st and 2nd order, respectively. The  
        surprisal can be parameterised with a  
        surprisal kernel K and then taking the outer product H = K’*K, where the  
        kernel K is parameterised to first-order. The solenoidal  
        (non-dissipative) parts of the flow operator are parameterised to 1st  
        order in the states. Alternatively the suprisal can be paramterised with  
        pE.Rp via a state dependant mean.  
         
        If pE.Gp = 0, it is assumed that the dissipative part of the flow (i.e.,  
        the amplitude of random fluctuations G) is spherical and constant. This  
        corresponds to the inverse precision of the random fluctuations that can  
        also be specified as M.W in the accompanying model M.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_NESS_priors.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_NESS_priors", *args, **kwargs)
