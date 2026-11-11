from spm._runtime import Runtime


def _tfcestat(*args, **kwargs):
    r"""
      TFCESTAT computes threshold-free cluster statistic for multidimensional  
        channel-freq-time or volumetric source data.  
         
        The configuration options that can be specified are:  
          cfg.tfce_method = 'exact' (default) or 'discrete'  
          cfg.tfce_H      = height exponent H (default 2)  
          cfg.tfce_E      = extent exponent E (default 0.5)  
          cfg.tfce_h0     = baseline/offset that is subtracted first (default 0)  
          cfg.tfce_nsteps = number of height steps for the 'discrete' method (default 100)  
          cfg.tail        = -1, 0 or 1 (default 0)  
         
        Two implementations are implemented, to be selected with cfg.tfce_method:  
         
          'exact'    (default) evaluates the TFCE integral EXACTLY (eTFCE). Because  
                     the cluster extent e(h) is piecewise constant in the height h  
                     (it changes only when h crosses a data value), the integral  
         
                         TFCE(v) = integral_{h0}^{h_v} e(h)^E * h^H dh  
         
                     has a closed form on each interval and is obtained in a single  
                     pass with a disjoint-set (union-find) cluster-retrieval forest,  
                     using the same spatial connectivity as FINDCLUSTER. This removes  
                     the cfg.tfce_nsteps discretisation (and its bias), is typically  
                     much faster than the threshold loop, and needs no SPM toolbox.  
         
          'discrete' the original implementation, which approximates the integral by  
                     summing over cfg.tfce_nsteps discrete height thresholds and  
                     calls FINDCLUSTER (which requires SPM) at each threshold. Kept for  
                     backward compatibility and for validating the exact method.  
         
        The exact-TFCE (eTFCE) algorithm was developed by Xu Chen, Wouter D. Weeda,  
        Thomas E. Nichols and Jelle J. Goeman (2026), "eTFCE: Exact Threshold-Free  
        Cluster Enhancement via Fast Cluster Retrieval", arXiv:2603.03004. The 'exact'  
        method below is a MATLAB implementation of that published algorithm for  
        FieldTrip; it was NOT created or developed by the implementer, who only  
        translated the method into code.  
         
        See also CLUSTERSTAT, FINDCLUSTER  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/tfcestat.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("tfcestat", *args, **kwargs)
