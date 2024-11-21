from spm.__wrapper__ import Runtime


def _meg_ini(*args, **kwargs):
    """
      initializes MEG-forward calculation  
        usage: forwpar=meg_ini(vc,center,order,sens,refs,gradlocs,weights)  
         
        input:  
        vc:  Nx6 matrix; N is the number of surface points  
             the first three numbers in each row  are the location  
             and the second three are the orientation of the surface  
             normal  
        center: 3x1 vector denoting the center of volume the conductor  
        order: desired order of spherical spherical harmonics;  
               for 'real' realistic volume conductors order=10 is o.k  
        sens:  Mx6 matrix containing sensor location and orientation,  
               format as for vc  
        refs: optional argument.  If provided, refs contains the location and oriantion  
              (format as sens) of additional sensors which are subtracted from the original  
               ones. This makes a gradiometer. One can also do this with the  
               magnetometer version of this program und do the subtraction outside this program,  
               but the gradiometer version is faster.  
        gradlocs, weights: optional two arguments (they must come together!).  
                           gradlocs are the location of additional  channels (e.g. to calculate  
                           a higher order gradiometer) and weights. The i.th row in weights contains  
                           the weights to  correct if the i.th cannel. These extra fields are added!  
                           (has historical reasons).  
         
        output:  
        forpwar: structure containing all parameters needed for forward calculation  
         
        note: it is assumed that locations are in cm.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/meg_ini.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("meg_ini", *args, **kwargs)
