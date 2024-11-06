from spm.__wrapper__ import Runtime


def spm_shoot_kernel(*args, **kwargs):
    """
      Generate kernel matrix from initial velocity fields  
        FORMAT spm_shoot_kernel(job)  
        job.velocities - Initial velocity fields  
        job.dotprod    - Part of filename for results  
         
        k(x_1,x_2) = <x_1,L x_2> = <L x_1, x_2>  
         
        This is very slow, and is not in a form that would be  
        suited to weighting according to location in the image.  
        For this, the "square root" of L would need to be used  
        in order to convert the flow fields into (e.g.) their  
        Jacobian tensor fields.  For linear elasticity, this  
        field would be decomposed by J = (J+J')/2 + (J-J')/2.  
        The elements of the symetric part (along with its trace)  
        would then be used to generate the kernel.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Shoot/spm_shoot_kernel.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_shoot_kernel", *args, **kwargs)
