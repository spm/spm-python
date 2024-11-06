from spm.__wrapper__ import Runtime


def spm_Lap2Lorenz(*args, **kwargs):
    """
      Laplace version of the Lorentz system  
        FORMAT [s,q,f] = spm_Lap2Lorenz(P,[w,x])  
        s - second order polynomial coefficients for(negative) potential  
        q - second-order polynomial coefficients for flow  
         
        this routine evaluates the Laplacian version of a Lorentz system with  
        supplied parameters in terms of second order polynomial coefficients.  
        This is an exact solution that conforms to the Helmholtz decomposition;  
        however, with an improper steady-state density due to the absence of a  
        leading diagonal Hessian. In the SPM code, the polynomial coefficients  
        for the flow operator include coefficients for the leading diagonal. This  
        means one can supplement any supplied dissipative or diagonal flow  
        operator with state-dependent terms (e.g., state-dependent random  
        fluctuations). The fixed values of these are specified in terms of the  
        precision of random fluctuations (i.e., G = 1/(2*w)  
       --------------------------------------------------------------------------  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_Lap2Lorenz.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_Lap2Lorenz", *args, **kwargs)
