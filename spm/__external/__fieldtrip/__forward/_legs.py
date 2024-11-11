from spm.__wrapper__ import Runtime


def _legs(*args, **kwargs):
    """
      usage: [basis,gradbasis]=legs(x,dir,n,scale)  
         
        returns the values and directional derivatives  of (n+1)^2-1 basis functions   
        constructed from spherical harmonics at locations given in x and, for the   
        gradients, for (in general non-normalized) directions given in dir.     
          
        input: x      set of N locations given as an Nx3 matrix   
               dir    set of N direction vectors given as an Nx3 matrix   
                         (dir is not normalized (it hence can be a dipole moment))  
               n       order of spherical harmonics   
         
        output: basis: Nx((n+1)^2-1)  matrix containing in the j.th  row the real   
                       and imaginary parts of r^kY_{kl}(theta,Phi)/(N_{kl}*scale^k) ( (r,theta,phi)   
                       are the spherical coordinates corresponding to  the j.th row in x)   
                       for k=1 to n and l=0 to k   
                       the order is:  
                                 real parts for k=1 and l=0,1 (2 terms)   
                         then    imaginary parts for k=1 and l=1 (1 term)   
                         then    real parts for k=2 and l=0,1,2 (3 terms)   
                         then    imaginary parts for k=2 and l=1,2 (2 term)   
                                     etc.  
                          the spherical harmonics are normalized with  
                          N_{kl}=sqrt(4pi (k+l)!/((k-l)!(2k+1)))  
                           the phase does not contain the usual (-1)^l term !!!   
                          scale is constant preferably set to the avererage radius                     
         
                gradbasis: Nx((n+1)^2-1) matrix containing in the j.th row the scalar   
                            product of the gradient of the former with the j.th row of dir  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/legs.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("legs", *args, **kwargs)
