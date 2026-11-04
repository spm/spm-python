from spm._runtime import Runtime


def _spikesort(*args, **kwargs):
    r"""
      SPIKESORT uses a variation on the cocktail sort algorithm in combination  
        with a city block distance to achieve N-D trial pairing between spike  
        counts. The sorting is not guaranteed to result in the optimal pairing. A  
        linear pre-sorting algorithm is used to create good initial starting  
        positions.  
         
        The goal of this function is to achieve optimal trial-pairing prior to  
        stratifying the spike numbers in two datasets by random removal of some  
        spikes in the trial and channel with the largest numnber of spikes.  
        Pre-sorting based on the city-block distance between the spike count  
        ensures that as few spikes as possible are lost.  
         
        Use as  
          [srtA, srtB, indA, indB] = spikesort(numA, numB, ...)  
         
        Optional arguments should be specified as key-value pairs and can include  
          'presort'  number representing the column, 'rowwise' or 'global'  
         
        Example  
          numA = reshape(randperm(100*3), 100, 3);  
          numB = reshape(randperm(100*3), 100, 3);  
          [srtA, srtB, indA, indB] = spikesort(numA, numB);  
          % check that the order is correct, the following should be zero  
          numA(indA,:) - srtA  
          numB(indB,:) - srtB  
         
        See also COCKTAILSORT  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/spikesort.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spikesort", *args, **kwargs)
