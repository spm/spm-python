from mpython import Runtime


def spm_eeg_headplot(*args, **kwargs):
    """
      SPM interface to headplot function from EEGLAB
        FORMAT spm_eeg_headplot(Y, D, H)

                Y - data vector
                D - M/EEG object
                H - (optional) axes handle

       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_eeg_headplot.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_headplot", *args, **kwargs, nargout=0)
