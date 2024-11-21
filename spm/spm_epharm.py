from spm.__wrapper__ import Runtime


def spm_epharm(*args, **kwargs):
    """
      basis set of prolate spheroidal harmonics  for modelling magnetic  
        interfecnce observed by point magnetometers.   
        FORMAT harmonics = spm_epharm(v,n,a,b,L)  
          v               - channel positions (nc x 3 matrix)     
          n               - channel orientations (nc x 3 matrix)    
          a               - semi-major axis length (1 x 1 matrix)   
          b               - semi-minor axis length (1 x 1 matrix)  
          L               - harmonic order (1 x 1 matrix)            
        Output:  
          harmonics       - prolate spheroidal harmonics spanning external space   
       __________________________________________________________________________  
        Copyright (C) 2023 Tim Tierney  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_epharm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_epharm", *args, **kwargs)
