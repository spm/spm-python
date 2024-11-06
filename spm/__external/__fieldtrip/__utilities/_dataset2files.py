from spm.__wrapper__ import Runtime


def _dataset2files(*args, **kwargs):
    """
      DATASET2FILES manages the filenames for the dataset, headerfile, datafile and eventfile  
        and tries to maintain a consistent mapping between them for each of the known fileformats  
         
        Use as  
          [filename, headerfile, datafile] = dataset2files(filename, format)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/dataset2files.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("dataset2files", *args, **kwargs)
