from mpython import Runtime


def _nearest_vec(*args, **kwargs):
    """
      locate bilateral coordinate
        Copyright (C) 2022 Wellcome Centre for Human Neuroimaging


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/private/nearest_vec.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("nearest_vec", *args, **kwargs)
