from mpython import Runtime


def spm_eeg_project3D(*args, **kwargs):
    """
      Wrapper function to a fieldtrip function to project 3D locations
        onto a 2D plane.
        FORMAT [xy,label] = spm_eeg_project3D(sens, modality)
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_project3D.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_project3D", *args, **kwargs)
