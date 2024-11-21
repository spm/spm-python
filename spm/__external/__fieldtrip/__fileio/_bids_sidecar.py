from spm.__wrapper__ import Runtime


def _bids_sidecar(*args, **kwargs):
    """
      BIDS_SIDECAR will search for corresponding BIDS sidecar files that go together with  
        a specific data file. This function respects the inheritance rules and will also  
        search higher up in the directory structure.  
         
        Use as  
          sidecar = bids_sidecar(filename, sidecar, extension)  
        where filename refers to a BIDS data file and suffix is a string that refers to the  
        specific sidecar file. To read the json sidecar corresponding to the data itself,  
        you can keep the suffix empty. In that case the suffix (e.g., meg or eeg) will  
        be determined from the filename.  
         
        This supports, but is not restricted to the following json sidecar files  
          'meg'  
          'eeg'  
          'ieeg'  
          'nirs'  
          'coordsystem'  
         
        This supports, but is not restricted to the following tsv sidecar files  
          'channels'  
          'electrodes'  
          'optodes'  
          'events'  
         
        You can specify the file extension (tsv or json) to be returned. When not specified  
        and in case both a tsv and a json sidecar file are present that match the suffix,  
        the tsv file will be returned.  
         
        See https://bids-specification.readthedocs.io/ for the specification and  
        http://bids.neuroimaging.io/ for background information.  
         
        See also BIDS_DATAFILE, BIDS_TSV, EVENTS_TSV, FT_READ_HEADER, FT_READ_EVENT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/bids_sidecar.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bids_sidecar", *args, **kwargs)
