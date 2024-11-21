from spm.__wrapper__ import Runtime


def spm_int_U(*args, **kwargs):
    """
      Integrate a MIMO nonlinear system (fast integration for sparse inputs)  
        FORMAT [y] = spm_int_U(P,M,U)  
        P   - model parameters  
        M   - model structure  
        U   - input structure or matrix  
         
        y   - (v x l)  response y = g(x,u,P)  
       __________________________________________________________________________  
        Integrates the MIMO system described by  
           
           dx/dt = f(x,u,P,M)  
           y     = g(x,u,P,M)  
          
        using the update scheme:  
         
           x(t + dt) = x(t) + U*dx(t)/dt  
         
                   U = (expm(dt*J) - I)*inv(J)  
                   J = df/dx  
         
        at input times.  This integration scheme is efficient because it  
        only evaluates the update matrix (Q) when the inputs change.  
        If f returns the Jacobian (i.e. [fx J] = feval(f,M.x,u,P,M) it will  
        be used.  Otherwise it is evaluated numerically.  
         
        spm_int will also handle static observation models by evaluating  
        g(x,u,P,M)  
         
         
       --------------------------------------------------------------------------  
         
        SPM solvers or integrators  
         
        spm_int_ode:  uses ode45 (or ode113) which are one and multi-step solvers  
        respectively.  They can be used for any ODEs, where the Jacobian is  
        unknown or difficult to compute; however, they may be slow.  
         
        spm_int_J: uses an explicit Jacobian-based update scheme that preserves  
        nonlinearities in the ODE: dx = (expm(dt*J) - I)*inv(J)*f.  If the  
        equations of motion return J = df/dx, it will be used; otherwise it is  
        evaluated numerically, using spm_diff at each time point.  This scheme is  
        infallible but potentially slow, if the Jacobian is not available (calls  
        spm_dx).  
         
        spm_int_E: As for spm_int_J but uses the eigensystem of J(x(0)) to eschew   
        matrix exponentials and inversion during the integration. It is probably  
        the best compromise, if the Jacobian is not available explicitly.  
         
        spm_int_B: As for spm_int_J but uses a first-order approximation to J  
        based on J(x(t)) = J(x(0)) + dJdx*x(t).  
         
        spm_int_L: As for spm_int_B but uses J(x(0)).  
         
        spm_int_U: like spm_int_J but only evaluates J when the input changes.  
        This can be useful if input changes are sparse (e.g., boxcar functions).  
        It is used primarily for integrating EEG models  
         
        spm_int:   Fast integrator that uses a bilinear approximation to the  
        Jacobian evaluated using spm_bireduce. This routine will also allow for  
        sparse sampling of the solution and delays in observing outputs. It is  
        used primarily for integrating fMRI models  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_int_U.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_int_U", *args, **kwargs)
