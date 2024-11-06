from spm.__wrapper__ import Runtime


def _readmarkerfile(*args, **kwargs):
    """
      Read the MarkerFile.mrk file in a CTF dataset.  
         
        Use as  
          marker = readmarkerfile(folder)  
         
        Creates a marker structure which contains number_markers,  
        number_samples, marker_names, and trial_times.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/readmarkerfile.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("readmarkerfile", *args, **kwargs)
