from mpython import Runtime


def cfg_example_run_div(*args, **kwargs):
    """
      Example function that returns the mod and rem of two numbers given in
        job.a and job.b in out.mod and out.rem.

        This code is part of a batch job configuration system for MATLAB. See
             help matlabbatch
        for a general overview.
       _______________________________________________________________________
        Copyright (C) 2007 Freiburg Brain Imaging


    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/examples/cfg_example_run_div.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("cfg_example_run_div", *args, **kwargs)
