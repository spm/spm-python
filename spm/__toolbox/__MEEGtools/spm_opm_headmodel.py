from spm.__wrapper__ import Runtime


def spm_opm_headmodel(*args, **kwargs):
    """
      Coregister FIL OPM data and option to set up forward model  
        FORMAT D = spm_opm_create(S)  
          S               - input structure  
        Fields of S:  
          S.D             - SPM MEEG Object                          - Default: REQUIRED   
          S.coordsystem   - coordsystem.json file                    - Default: transform between sensor space and anatomy is identity  
          S.sMRI          - Filepath to  MRI file                    - Default: no Default  
          S.template      - Use SPM canonical template               - Default: 0  
          S.headhape      - .pos file for better template fit        - Default: no Default  
          S.cortex        - Custom cortical mesh                     - Default: Use inverse normalised cortical mesh  
          S.scalp         - Custom scalp mesh                        - Default: Use inverse normalised scalp mesh  
          S.oskull        - Custom outer skull mesh                  - Default: Use inverse normalised outer skull mesh  
          S.iskull        - Custom inner skull mesh                  - Default: Use inverse normalised inner skull mesh  
          S.voltype       - Volume conducter Model type              - Default: 'Single Shell'  
          S.meshres       - mesh resolution(1,2,3)                   - Default: 1  
          S.lead          - flag to compute lead field               - Default: 0  
        Output:  
         D           - MEEG object (also written to disk)  
         L           - Lead field (also written on disk)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_opm_headmodel.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_opm_headmodel", *args, **kwargs)
