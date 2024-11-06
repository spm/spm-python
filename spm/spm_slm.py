from spm.__wrapper__ import Runtime


def spm_slm(*args, **kwargs):
    """
      basis set of spehrical harmonics and their (optional) angular derivatives  
        as observed by point magnetometers.   
        FORMAT [slm,dslmdphi,dslmdtheta] = spm_slm(theta,phi,li)  
          theta             - colattitude (nchannel x 1 matrix)   
          phi               - longitude   (nchannel x 1 matrix)   
          li                - harmonic order (1 x 1 matrix)   
        Output:  
          slm          - spherical harmonics  
          dslmdphi     - derivative with respecte to longitude  
          dslmdtheta   - derivative with respecte to lattitude  
       __________________________________________________________________________  
        Copyright (C) 2023 Tim Tierney  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_slm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_slm", *args, **kwargs)
