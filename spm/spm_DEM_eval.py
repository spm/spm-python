from spm.__wrapper__ import Runtime


def spm_DEM_eval(*args, **kwargs):
    """
      Evaluate state equations and derivatives for DEM schemes  
        FORMAT [E,dE,f,g] = spm_DEM_eval(M,qu,qp)  
         
        M  - model structure  
        qu - conditional mode of states  
         qu.v{i} - casual states  
         qu.x(i) - hidden states  
         qu.y(i) - response  
         qu.u(i) - input  
        qp - conditional density of parameters  
         qp.p{i} - parameter deviates for i-th level  
         qp.u(i) - basis set  
         qp.x(i) - expansion point ( = prior expectation)  
         
        E  - generalised errors  (i.e.., y - g(x,v,P); x[1] - f(x,v,P))  
         
        dE:  
         dE.du   - de[1:n]/du  
         dE.dy   - de[1:n]/dy[1:n]  
         dE.dc   - de[1:n]/dc[1:d]  
         dE.dp   - de[1:n]/dp  
         dE.dup  - d/dp[de[1:n]/du  
         dE.dpu  - d/du[de[1:n]/dp  
         
        where u = x{1:d]; v[1:d]  
         
        To accelerate computations one can specify the nature of the model using  
        the field:  
         
        M(1).E.linear = 0: full        - evaluates 1st and 2nd derivatives  
        M(1).E.linear = 1: linear      - equations are linear in x and v  
        M(1).E.linear = 2: bilinear    - equations are linear in x, v & x*v  
        M(1).E.linear = 3: nonlinear   - equations are linear in x, v, x*v, & x*x  
        M(1).E.linear = 4: full linear - evaluates 1st derivatives (for generalised   
                                         filtering, where parameters change)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_DEM_eval.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_DEM_eval", *args, **kwargs)
