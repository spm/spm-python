from mpython import Runtime


def spm_topo_lookup(*args, **kwargs):
    """
      Create a topology change lookup table
        FORMAT lkp = spm_topo_lookup
        lkp - The lookup table of 1s and 0s.

        The table is used for determining whether erosion can be
        done without changing local topology. In addition to returning
        lkp, it is also saved in a topol_lookup.mat file.

        The code is not very efficient, so the lookup table takes about
        a day and a half to compute.
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Spatial/spm_topo_lookup.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_topo_lookup", *args, **kwargs)
