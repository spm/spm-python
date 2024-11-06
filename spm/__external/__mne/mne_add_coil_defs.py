from spm.__wrapper__ import Runtime


def mne_add_coil_defs(*args, **kwargs):
    """
       
        [res] = mne_add_coil_defs(chs,accuracy,coil_def_templates)  
         
        Add transformed coil definitions to the channel info  
         
        chs        - original channel definitions  
        accuracy   - desired accuracy (0, 1, or 2, defaults to 1)  
        templates  - coil definition templates  
                     (defaults to $MNE_ROOT/setup/mne/coil_def.dat or $MNE_ROOT/share/mne/coil_def.dat)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_add_coil_defs.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mne_add_coil_defs", *args, **kwargs)
