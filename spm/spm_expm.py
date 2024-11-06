from spm.__wrapper__ import Runtime


def spm_expm(*args, **kwargs):
    """
      Approximate matrix exponential using a Taylor expansion  
        FORMAT [y] = spm_expm(J,x)  
        FORMAT [y] = spm_expm(J)  
        y          = expm(J)*x:  
        y          = expm(J);  
         
        This routine covers and extends expm  functionality  by  using  a  
        comoutationally  expedient  approximation  that can handle sparse  
        matrices when dealing with the special case of expm(J)*x, where x  
        is a vector, in an efficient fashion  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_expm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_expm", *args, **kwargs)
