from mpython import Runtime


def spm_eeg_meshnative2mni(*args, **kwargs):
    """
     function nativemesh=spm_eeg_meshmni2native(mnimesh,mesh)
        Uses mesh ( spm mesh structure D.inv{:}.mesh ) to compute transform to
        express mnimesh in native space
        replicates code segment from headmodel section of SPM code


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_meshnative2mni.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_meshmni2native", *args, **kwargs)
