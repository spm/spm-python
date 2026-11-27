from spm._runtime import Runtime


def _dataset2files(*args, **kwargs):
    r"""
      DATASET2FILES manages the filenames for the dataset, headerfile, datafile and eventfile  
        and tries to maintain a consistent mapping between them for each of the known fileformats  
         
        Use as  
          [filename, headerfile, datafile] = dataset2files(filename, format)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/dataset2files.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("dataset2files", *args, **kwargs)
