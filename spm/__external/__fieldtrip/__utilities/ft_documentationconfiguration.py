from mpython import Runtime


def ft_documentationconfiguration(*args, **kwargs):
    """
      FT_DOCUMENTATIONCONFIGURATION is a helper function to maintain the online
        documentation of all configuration options.

        Normal users will not be calling this function, but will rather look at
        http://www.fieldtriptoolbox.org/configuration where the output of this
        function can be found.

        See also FT_DOCUMENTATIONREFERENCE


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_documentationconfiguration.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_documentationconfiguration", *args, **kwargs)
