from spm.__wrapper__ import Runtime


def spm_ness(*args, **kwargs):
    """
      Evaluation of hessian and solenoidal operators at NESS  
        FORMAT [H,R]     = spm_ness(J,G)  
        FORMAT [H,R,J,G] = spm_ness(J,G)   %%%% complex  
        J  - Jacobian (dfdx)  
        G  - diffusion tensor (amplitude of random fluctuations)  
         
        H  - Hessian matrix (i.e., precision of a Gaussian density)  
        R  - Skew symmetric solenoidal operator (-Q')  
         
        if called with four output arguments, complex forms are returned  
       __________________________________________________________________________  
        This routine evaluates the Hessian (i.e., precision) of a nonequilibrium  
        steady-state density (using a local linear approximation, under Gaussian  
        assumptions). This is evaluated  under linear constraints on the  
        solenoidal term of a Helmholtz decomposition. In short, given the flow  
        (encoded by the systems Jacobian) and amplitude of random fluctuations,  
        one can evaluate the steady-state density under nonequilibrium dynamics  
        implied by solenoidal flow.  
         
        There are additional notes using symbolic maths and numerical examples in  
        the main body of the script.  
         
        flow constraints (Jacobian J)(R = -Q')  
       --------------------------------------------------------------------------  
        where flow   f = (R + G)*d log(p(x))/dx and  
        log(p(x))      = -(1/2)*x'*H*x =>  
        d log(p(x))/dx = -H*x =>  
        df/dx = J      = -(R + G)*H =>  
        H              = -(R + G)\J =>  
        J*R + R*J'     = J*G - G*J'  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_ness.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_ness", *args, **kwargs)
