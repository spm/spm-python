from spm._runtime import Runtime


def spm_mci_sens_sun(*args, **kwargs):
    """
      As spm_mci_sens.m but using Sundials  
        FORMAT [y,sy,st,x,sx] = spm_mci_sens_sun (P,M,U,csx)  
         
        P         Parameters  
        M         Model structure  
        U         Inputs  [Nin x N]  
        csx       Set to 1 to compute state sensitivity  
              
        y         Outputs     [N x Nout]  
        sy        Output Sensitivity, dy/dP [N x Nout x Nparams]  
        st        Status flag (0 for success, -1 for problem)  
        x         States      [N x Nstates]  
        sx        State Sensitivity, dx/dP [N x Nstates x Nparams]  
                  ... evaluated at the N time points in M.t  
         
        M.f       Flow function dx/dt=f(x,u,P,M)  
        M.g       Observation function y=g(x,u,P,M)  
         
        This function uses the sundials package (CVODE,CVODES,IDA,IDAS)  
        from http://computation.llnl.gov/casc/sundials/main.html  
         
        B. Sengupta, K. Friston and W. Penny (2014) Efficient Gradient  
        Computation for Dynamical Models. Neuroimage,98, 521-527.   
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/gradients/spm_mci_sens_sun.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mci_sens_sun", *args, **kwargs)
