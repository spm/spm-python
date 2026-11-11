from spm._runtime import Runtime


def _leadfield_fns(*args, **kwargs):
    r"""
      LEADFIELD_FNS calculates the FDM forward solution for a set of given  
        dipolar sources  
         
        [lf] = leadfield_fns(posin, vol, tol);  
         
        with input arguments  
          dip    positions of the dipolar sources (MX3 matrix)  
          vol    structure of the volume conductor  
          tol    tolerance  
          
        The output argument lf   
          
        The key elements of the vol structure are:  
          vol.condmatrix a 9XT (T tissues) matrix containing the conductivities  
          vol.seg        a segmented/labelled MRI  
          vol.deepelec   positions of the deep electrodes (NX3 matrix)  
           or  
          vol.bnd        positions of the external surface vertices  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/forward/private/leadfield_fns.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("leadfield_fns", *args, **kwargs)
