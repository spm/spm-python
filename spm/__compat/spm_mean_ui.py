from mpython import Runtime


def spm_mean_ui(*args, **kwargs):
    """
      Prompt for a series of images and averages them
       __________________________________________________________________________

        This function is deprecated. Use spm_mean instead.
       __________________________________________________________________________
        Copyright (C) 1998-2011 Wellcome Trust Centre for Neuroimaging


    [Matlab code]( https://github.com/spm/spm/blob/main/compat/spm_mean_ui.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mean_ui", *args, **kwargs, nargout=0)
