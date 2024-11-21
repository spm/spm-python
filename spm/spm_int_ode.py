from spm.__wrapper__ import Runtime


def spm_int_ode(*args, **kwargs):
    """
      Integrate a MIMO nonlinear system (using classical ODE solvers)  
        FORMAT [y] = spm_int_ode(P,M,U)  
        P   - model parameters  
        M   - model structure  
        U   - input structure or matrix  
         
        y   - (v x l)  response y = g(x,u,P)  
       __________________________________________________________________________  
        Integrates the MIMO system described by  
         
           dx/dt = f(x,u,P,M)  
           y     = g(x,u,P,M)  
         
        using an Runge-Kutta(4,5) scheme over the times implicit in the input.  
        ode45 is based on an explicit Runge-Kutta (4,5) formula, the Dormand-  
        Prince pair. It is a one-step solver - in computing y(tn), it needs only   
        the solution at the immediately preceding time point y(tn-1). In general,  
        ode45 is the best function to apply as a "first try" for most problems.  
         
        ode113 is a variable order Adams-Bashforth-Moulton PECE solver. It may be  
        more efficient than ode45 at stringent tolerances and when the ODE file   
        function is particularly expensive to evaluate. ode113 is a multi-step   
        solver - it normally needs the solutions at several preceding time points  
        to compute the current solution  
         
        see also ode45; ode113  
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
         
        spm_int_U: like spm_int_J but only evaluates J when the input changes.  
        This can be useful if input changes are sparse (e.g., boxcar functions).  
        spm_int_U also has the facility to integrate delay differential equations  
        if a delay operator is returned [f J D] = f(x,u,P,M)  
         
        spm_int:   Fast integrator that uses a bilinear approximation to the   
        Jacobian evaluated using spm_bireduce. This routine will also allow for  
        sparse sampling of the solution and delays in observing outputs  
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_int_ode.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_int_ode", *args, **kwargs)
