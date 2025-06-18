from mpython import Runtime


def _bids_datafile(*args, **kwargs):
    """
      BIDS_DATAFILE will search for the data file, given one of the corresponding sidecar files

        Use as
          [datafile, jsonfile] = bids-datafile(filename)

        See also BIDS_SIDECAR, BIDS_TSV, EVENTS_TSV


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/bids_datafile.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bids_datafile", *args, **kwargs)
