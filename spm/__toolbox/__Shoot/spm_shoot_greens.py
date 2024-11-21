from spm.__wrapper__ import Runtime


def spm_shoot_greens(*args, **kwargs):
    """
      Build and apply FFT of Green's function (to map from momentum to velocity)  
        FORMAT v = spm_shoot_greens(m,K,prm)  
        m    - Momentum field n1*n2*n3*3 (single prec. float)  
        K    - Fourier transform representation of Green's function  
               - either size n1*n2*n3 or n1*n2*n3*3*3  
        prm  - Differential operator parameters (3 voxel sizes, 5 hyper-parameters)  
               - only needed when K is of size n1*n2*n3, in which case, voxel sizes  
                 are necessary for dealing with each component individually  
        v    - velocity field  
         
        FORMAT [K,ld] = spm_shoot_greens('kernel',dm,prm)  
        dm  - dimensions n1*n2*n3  
        prm - Differential operator parameters (3 voxel sizes, 5 hyper-parameters)  
        K   - Fourier transform representation of Green's function  
               - either size n1*n2*n3 or n1*n2*n3*3*3  
        ld(1)  - Log determinant of operator  
        ld(2)  - Number of degrees of freedom  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Shoot/spm_shoot_greens.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_shoot_greens", *args, **kwargs)
