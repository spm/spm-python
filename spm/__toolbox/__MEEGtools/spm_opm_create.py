from spm._runtime import Runtime


def spm_opm_create(*args, **kwargs):
    """
      Read magnetometer data and optionally set up forward model  
        FORMAT [D,L] = spm_opm_create(S)  
          S               - input structure  
        Optional fields of S:  
        SENSOR LEVEL INFO  
          S.data          - filepath/matrix(nchannels x timepoints)  - Default:required  
          S.channels      - channels.tsv file                        - Default: REQUIRED unless data is from neuro-1 system  
          S.fs            - Sampling frequency (Hz)                  - Default: REQUIRED if S.meg is empty  
          S.meg           - meg.json file                            - Default: REQUIRED if S.fs is empty  
          S.precision     - 'single' or 'double'                     - Default: 'single'  
        SOURCE LEVEL INFO  
          S.coordsystem   - coordsystem.json file                    - Default: transform between sensor space and anatomy is identity  
          S.positions     - positions.tsv file                       - Default: no Default  
          S.sMRI          - Filepath to  MRI file                    - Default: no Default  
          S.template      - Use SPM canonical template               - Default: 0  
          S.headhape      - .pos file for better template fit        - Default:  
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_opm_create.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_opm_create", *args, **kwargs)
