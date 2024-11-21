from spm.__wrapper__ import Runtime


def _svdfft(*args, **kwargs):
    """
      SVDFFT computes a rotated FFT matrix, using the real part of the cross-spectral  
        density matrix. This rotation ensures that the phase relationship of the underlying  
        sources does not change, while rotating the channels such that the first channel  
        contains the maximal amplitude signal.  
         
        Use as  
          [fr, ut] = svdfft(f, n, trltapcnt);  
        where  
          n           number of components (orientations) to keep in the output (e.g. 1, 2 or 3)  
          trltapcnt   vector of length Ntrials with the number of tapers  
         
        See also SVD  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/svdfft.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("svdfft", *args, **kwargs)
