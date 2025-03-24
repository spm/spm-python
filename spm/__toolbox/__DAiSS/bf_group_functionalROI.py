from mpython import Runtime


def bf_group_functionalROI(*args, **kwargs):
    """
      Computes Minimum Norm projectors

        Please cite:
        Hauk O, Stenroos M.
        A framework for the design of flexible cross-talk functions for spatial
        filtering of EEG/MEG data: DeFleCT.
        Human Brain Mapping 2013
        http://imaging.mrc-cbu.cam.ac.uk/meg/AnalyzingData/DeFleCT_SpatialFiltering_Tools
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_group_functionalROI.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bf_group_functionalROI", *args, **kwargs)
