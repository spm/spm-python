from spm.__wrapper__ import Runtime


def spm_mesh_euler(*args, **kwargs):
    """
      Compute the Euler characteristic of a triangle mesh  
        M        - patch structure  
         
        X        - Euler characteristic  
       __________________________________________________________________________  
         
        The Euler characteristic is defined according to the formula:  
         
                           X  =  V - E + F  =  2 - 2g - b  
         
        where g is the genus and b the number of boundary components.  
        See https://www.wikipedia.org/wiki/Euler_characteristic  
            https://www.wikipedia.org/wiki/Genus_(mathematics)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mesh_euler.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mesh_euler", *args, **kwargs)
