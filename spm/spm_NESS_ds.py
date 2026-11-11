from spm._runtime import Runtime


def spm_NESS_ds(*args, **kwargs):
    r"""
      Generate changes in log density (coefficients or at x)  
        FORMAT [dS,G,Q,L] = spm_NESS_ds(Sp,P)  
        FORMAT [ds,G,Q,L] = spm_NESS_ds(Sp,P,x)  
        FORMAT [ds,G,Q,L] = spm_NESS_ds(Sp,P,U)  
       --------------------------------------------------------------------------  
        Sp      - polynomial coefficients of initial potential  
        P.Qp    - polynomial coefficients of solenoidal operator  
        P.Sp    - polynomial coefficients of final potential  
        P.G     - amplitude of random fluctuations  
         
        x       - sample points and state space  
         
        dS      - time derivative of polynomial coefficients of potential  
        ds      - time derivative of potential at x  
        G       - dissipation operator  
        Q       - solenoidal operator  
        L       - correction term for derivatives of solenoidal flow  
         
        This routine assumes that K = 3; i.e., the log density is second order in  
        the states (Laplace assumption). if called with two arguments the time  
        derivatives of the (second-order) polynomial coefficients of the log  
        density are returned. If called with three arguments, the time derivative  
        of the log density at the specified points in state space are returned.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_NESS_ds.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_NESS_ds", *args, **kwargs)
