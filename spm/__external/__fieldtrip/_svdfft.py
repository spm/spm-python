from spm.__wrap__ import _Runtime


def _svdfft(*args, **kwargs):
  """  SVDFFT computes a rotated FFT matrix, using the real part of the cross-spectral  
    density matrix. This rotation ensures that the phase relationship of the underlying  
    sources does not change, while rotating the channels such that the first channel  
    contains the maximal amplitude signal.  
     
    Use as  
      [fr, ut] = svdfft(f, n, trltapcnt);  
    where  
      n           number of components (orientations) to keep in the output (e.g. 1, 2 or 3)  
      trltapcnt   vector of length Ntrials with the number of tapers  
     
    See also SVD  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/svdfft.m)
  """

  return _Runtime.call("svdfft", *args, **kwargs)
