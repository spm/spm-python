from spm.__wrapper__ import Runtime


def _event2boolvec(*args, **kwargs):
    """
      EVENT2BOOLVEC converts between two representations of events or trials.  
         
        FieldTrip uses a number of representations for events that are conceptually very similar  
          event    = structure with type, value, sample, duration and offset  
          trl      = Nx3 numerical array with begsample, endsample, offset  
          trl      = table with 3 columns for begsample, endsample, offset  
          artifact = Nx2 numerical array with begsample, endsample  
          artifact = table with 2 columns for begsample, endsample  
          boolvec  = 1xNsamples boolean vector with a thresholded TTL/trigger sequence  
          boolvec  = MxNsamples boolean matrix with a thresholded TTL/trigger sequence  
         
        If trl or artifact are represented as a MATLAB table, they can have additional  
        columns. These additional columns have to be named and are not restricted to  
        numerical values.  
         
        See also ARTIFACT2BOOLVEC, ARTIFACT2EVENT, ARTIFACT2TRL, BOOLVEC2ARTIFACT, BOOLVEC2EVENT, BOOLVEC2TRL, EVENT2ARTIFACT, EVENT2BOOLVEC, EVENT2TRL, TRL2ARTIFACT, TRL2BOOLVEC, TRL2EVENT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/event2boolvec.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("event2boolvec", *args, **kwargs)
