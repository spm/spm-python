from spm._runtime import Runtime


def _circularcoil(*args, **kwargs):
    r"""
      CIRCULARCOIL magnetic field of a circular current loop  
         
        Use as:  
          [Bx, By, Bz] = circularcoil(x, y, z, d, I)  
         
        where  
          x,y,z : observation point(s) [m]  
          d     : coil diameter [m]  
          I     : coil current [A]  
        and  
          Bx,By,Bz : magnetic field components [T]  
         
        The coil is centered at (0,0,0), lies in the xy-plane,  
        and carries current I. Positive I gives a field in +z  
        at the center.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/forward/private/circularcoil.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("circularcoil", *args, **kwargs)
