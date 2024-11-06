from spm.__wrapper__ import Runtime


def _splint(*args, **kwargs):
    """
      SPLINT computes the spherical spline interpolation and the surface laplacian  
        of an EEG potential distribution  
          
        Use as  
          [V2, L2, L1] = splint(elc1, V1, elc2)  
        where  
          elc1    electrode positions where potential is known  
          elc2    electrode positions where potential is not known  
          V1      known potential  
        and  
          V2      potential at electrode locations in elc2  
          L2      laplacian of potential at electrode locations in elc2  
          L1      laplacian of potential at electrode locations in elc1  
          order   order of splines  
          degree  degree of Legendre polynomials  
          lambda  regularization parameter  
         
        See also LAPINT, LAPINTMAT, LAPCAL  
        This implements  
          F. Perrin, J. Pernier, O. Bertrand, and J. F. Echallier.  
          Spherical splines for scalp potential and curernt density mapping.  
          Electroencephalogr Clin Neurophysiol, 72:184-187, 1989.  
        including their corrections in   
          F. Perrin, J. Pernier, O. Bertrand, and J. F. Echallier.  
          Corrigenda: EEG 02274, Electroencephalography and Clinical  
          Neurophysiology 76:565.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/splint.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("splint", *args, **kwargs)
