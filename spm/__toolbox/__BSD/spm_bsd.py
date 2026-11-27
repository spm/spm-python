from spm._runtime import Runtime


def spm_bsd(*args, **kwargs):
    r"""
      Estimate parameters of a Bayesian Spectral Decomposition model of   
        (complex) cross-spectral density  
        FORMAT BSD = spm_bsd(BSD)  
         
        BSD  
           name: name string  
              xY: data   [1x1 struct]  
              xU: design [1x1 struct]  
         
          Sname: cell of source name strings  
         
          options.Nmodes       - number of spatial modes  
          options.Tdcm         - [start end] time window in ms  
          options.Fdcm         - [start end] Frequency window in Hz  
          options.D            - time bin decimation       (usually 1 or 2)  
          options.separatenull - bool, whether to fit null model separately  
          options.fitlog       - bool, fit log power spectra  
          options.powerline    - [start end] filter with low precision  
         
        Esimates:  
       --------------------------------------------------------------------------  
        BSD.dtf                   - directed transfer functions (source space)  
        BSD.ccf                   - cross covariance functions (source space)  
        BSD.coh                   - cross coherence functions (source space)  
        BSD.fsd                   - specific delay functions (source space)  
        BSD.pst                   - peristimulus time  
        BSD.Hz                    - frequency  
         
        BSD.Ep                    - conditional expectation  
        BSD.Cp                    - conditional covariance  
        BSD.Pp                    - conditional probability  
        BSD.Hc                    - conditional responses (y), channel space  
        BSD.Rc                    - conditional residuals (y), channel space  
        BSD.Hs                    - conditional responses (y), source space  
        BSD.Ce                    - eML error covariance  
        BSD.F                     - Laplace log evidence  
        BSD.ID                    -  data ID  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/BSD/spm_bsd.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_bsd", *args, **kwargs)
