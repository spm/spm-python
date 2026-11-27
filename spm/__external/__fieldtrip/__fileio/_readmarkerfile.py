from spm._runtime import Runtime


def _readmarkerfile(*args, **kwargs):
    r"""
      Read the MarkerFile.mrk file in a CTF dataset.  
         
        Use as  
          marker = readmarkerfile(folder)  
         
        Creates a marker structure which contains number_markers,  
        number_samples, marker_names, and trial_times.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/readmarkerfile.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("readmarkerfile", *args, **kwargs)
