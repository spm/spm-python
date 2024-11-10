from spm.__wrapper__ import Runtime


def spm_dartel_integrate(*args, **kwargs):
    """
      Integrate a Dartel flow field  
        FORMAT [Phi,DPhi] = spm_dartel_exp(U,t,K)  
            U    - name of flow field (nx x ny x nz x nt x 3)  
            t    - [t0 t1] Start and end time (values between 0 and 1)  
            K    - log2 of the Euler time steps to integrate the  
                   flow field.  
         
            Phi  - deformation field (nx x ny x nz x 3)  
            DPhi - Jacobian determinant field (nx x ny x nz)  
         
        The function integrates  
            Phi(x,t) = \int_{t_0}^{t_1} U(Phi(x,t),t) dt  
        where U is a piecewise constant flow field  
         
        Note: this function is ready for LDDMM-style flow fields, even  
        though the none of the official Dartel tools can generate them  
        yet.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dartel_integrate.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dartel_integrate", *args, **kwargs)
