from spm._runtime import Runtime


def _bf_fuse_lf(*args, **kwargs):
    """
      Prepares lead-fields to match channels in covariance  
        Copyright (C) 2014 Wellcome Trust Centre for Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/private/bf_fuse_lf.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_fuse_lf", *args, **kwargs)
