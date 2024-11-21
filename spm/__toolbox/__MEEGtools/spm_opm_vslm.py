from spm.__wrapper__ import Runtime


def spm_opm_vslm(*args, **kwargs):
    """
      cartesian real regular/irregular vector spherical harmonics  
        FORMAT vSlm   =  spm_opm_vslm(S)  
          S               - input structure  
        Optional fields of S:  
        SENSOR LEVEL INFO  
          S.D         - SPM MEEG object      - Default: specify S.D or, S.v and S.o  
          S.v         - optional positions               - Default: same as S.D  
          S.o         - optional orientations            - Default: same as S.D  
          S.or        - optional origin offset           - Default = [0,0,0]  
          S.reg       - regular or irregular (boolean)   - Default: 1  
          S.scale     - scale harmonic for stabilty      - Default: 1  
          S.li        - order of harmonic                - Default: 1  
        Output:  
         vSlm            - matrix of vector spherical harmonic (n x (li^2+2*l))  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_opm_vslm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_opm_vslm", *args, **kwargs)
