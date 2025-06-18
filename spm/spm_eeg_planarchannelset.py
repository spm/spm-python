from mpython import Runtime


def spm_eeg_planarchannelset(*args, **kwargs):
    """
      Define the planar gradiometer channel combinations
        FORMAT planar = spm_eeg_planarchannelset(data)

        The output cell array contains the horizontal label, vertical label and
        the label after combining the two.
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_planarchannelset.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_planarchannelset", *args, **kwargs)
