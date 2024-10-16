from spm.__wrapper__ import Runtime


def _dataset2files(*args, **kwargs):
  """  DATASET2FILES manages the filenames for the dataset, headerfile, datafile and eventfile  
    and tries to maintain a consistent mapping between them for each of the known fileformats  
     
    Use as  
      [filename, headerfile, datafile] = dataset2files(filename, format)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/dataset2files.m)
  """

  return Runtime.call("dataset2files", *args, **kwargs)
