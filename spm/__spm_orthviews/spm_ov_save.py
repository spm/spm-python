from mpython import Runtime


def spm_ov_save(*args, **kwargs):
    """
      Save as image tool - plugin for spm_orthviews

        This routine is a plugin to spm_orthviews. For general help about
        spm_orthviews and plugins type
                    help spm_orthviews
        at the MATLAB prompt.
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_orthviews/spm_ov_save.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_ov_save", *args, **kwargs)
