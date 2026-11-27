from spm._runtime import Runtime


def spm_eeg_invert_display(*args, **kwargs):
    r"""
      Displays conditional expectation of response (J)  
        FORMAT spm_eeg_invert_display(D,PST,Ndip)  
        FORMAT spm_eeg_invert_display(D,XYZ,Ndip)  
        D    - 3D structure (ReML estimation of response (J) )  
        PST  - peristimulus time (ms) - defaults to the PST of max abs(J)  
             - [Start Stop] (ms)     - invokes a movie of CSD  
        XYZ  - dipole location of interest  
         
        Ndip - number of dipole to display (default 512)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_invert_display.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_invert_display", *args, **kwargs, nargout=0)
