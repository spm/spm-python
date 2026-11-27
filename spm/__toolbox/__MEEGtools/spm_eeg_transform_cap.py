from spm._runtime import Runtime


def spm_eeg_transform_cap(*args, **kwargs):
    r"""
      Transform an electrode cap to match the subject's headshape  
        FORMAT shape = spm_eeg_transform_cap(S)  
         
        S                    - input structure (optional)  
        (optional) fields of S:  
          S.standard         - headshape (file) with the standard locations  
          S.custom           - headshape (file) with individually measured locations  
          S.outfile          - file name to save the output                       
         
        Output:  
          sens               - transformed sensors  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/MEEGtools/spm_eeg_transform_cap.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_transform_cap", *args, **kwargs)
