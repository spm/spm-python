from spm.__wrapper__ import Runtime


def spm_eeg_meshnative2mni(*args, **kwargs):
    """
     function mnimesh=spm_eeg_meshnative2mni(nativemesh,mesh)  
        Uses mesh ( spm mesh structure D.inv{:}.mesh ) to compute transform to   
        express  
        nativemesh(gifti filename) in native MRI space  
        as  
        mnimesh as gitfi structure in mni space  
        replicates code segment from headmodel section of SPM code  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_meshnative2mni.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_meshnative2mni", *args, **kwargs)
