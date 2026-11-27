from spm._runtime import Runtime


def _bids_datafile(*args, **kwargs):
    r"""
      BIDS_DATAFILE will search for the data file, given one of the corresponding sidecar files  
         
        Use as  
          [datafile, jsonfile] = bids-datafile(filename)  
         
        See also BIDS_SIDECAR, BIDS_TSV, EVENTS_TSV  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/bids_datafile.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bids_datafile", *args, **kwargs)
