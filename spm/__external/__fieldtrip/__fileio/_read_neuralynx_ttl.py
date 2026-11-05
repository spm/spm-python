from spm._runtime import Runtime


def _read_neuralynx_ttl(*args, **kwargs):
    r"""
      READ_NEURALYNX_TTL reads the Parallel_in values from a *.ttl file  
         
        Use as  
          [dat] = read_neuralynx_ttl(filename, begsample, endsample);  
         
        The *.ttl file is not a formal Neuralynx file format, but at the  
        F.C. Donders Centre we use it in conjunction with Neuralynx and  
        SPIKEDOWNSAMPLE.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_neuralynx_ttl.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_neuralynx_ttl", *args, **kwargs)
