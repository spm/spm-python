from spm.__wrapper__ import Runtime


def spm_shoot3di(*args, **kwargs):
    """
      Geodesic shooting  
        FORMAT [theta,Jtheta,v1,phi,Jphi] = spm_shoot3di(v0,prm,args)  
        v0     - Initial velocity field n1*n2*n3*3 (single prec. float)  
        prm  - 8 settings  
               - [1][2][3] Voxel sizes  
               - [4][5][6][7][8] Regularisation settings.  
                 Regularisation uses the sum of  
                 - [4] - absolute displacements  
                 - [5] - laplacian  
                 - [6] - bending energy  
                 - [7] - linear elasticity mu  
                 - [8] - linear elasticity lambda  
        args   - Integration parameters  
                 - [1] Num time steps  
         
        theta  - Inverse deformation field n1*n2*n3*3 (single prec. float)  
        Jtheta - Inverse Jacobian tensors n1*n2*n3 (single prec. float)  
        v1     - Final velocity field n1*n2*n3*3 (single prec. float)  
        phi    - Forward deformation field n1*n2*n3*3 (single prec. float)  
        Jphi   - Forward Jacobian tensors n1*n2*n3 (single prec. float)  
         
        This code generates deformations and their Jacobian determinans from  
        initial velocity fields by gedesic shooting.  See the work of Miller,  
        Younes and others.  
         
        LDDMM (Beg et al) uses the following evolution equation:  
            d\phi/dt = v_t(\phi_t)  
        where a variational procedure is used to find the stationary solution  
        for the time varying velocity field.  
        In principle though, once the initial velocity is known, then the  
        velocity at subsequent time points can be computed.  This requires  
        initial momentum (m_0), computed (using differential operator L) by:  
            m_0 = L v_0  
        Then (Ad_{\phi_t})^* m_0 is computed:  
            m_t = |d \phi_t| (d\phi_t)^T m_0(\phi_t)  
        The velocity field at this time point is then obtained by using  
        multigrid to solve:  
            v_t = L^{-1} m_t  
         
        These equations can be found in:  
        Younes (2007). "Jacobi fields in groups of diffeomorphisms and  
        applications". Quarterly of Applied Mathematics, vol LXV,  
        number 1, pages 113-134 (2007).  
         
        Multigrid is currently used to obtain v_t = L^{-1} m_t, but  
        this could also be done by convolution with the Greens function  
        N = L^{-1} (see e.g. Bro-Nielson).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Shoot/spm_shoot3di.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_shoot3di", *args, **kwargs)
