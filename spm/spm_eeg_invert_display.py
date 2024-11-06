from spm.__wrapper__ import Runtime


def spm_eeg_invert_display(*args, **kwargs):
    """
      Displays conditional expectation of response (J)  
        FORMAT spm_eeg_invert_display(D,PST,Ndip)  
        FORMAT spm_eeg_invert_display(D,XYZ,Ndip)  
        D    - 3D structure (ReML estimation of response (J) )  
        PST  - peristimulus time (ms) - defaults to the PST of max abs(J)  
             - [Start Stop] (ms)     - invokes a movie of CSD  
        XYZ  - dipole location of interest  
         
        Ndip - number of dipole to display (default 512)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_invert_display.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_invert_display", *args, **kwargs, nargout=0)
