from spm.__wrapper__ import Runtime


def bf_stat_evoked_t(*args, **kwargs):
    """
      Compute t-stat accross trials for evoked response  
        FORMAT BF = bf_stat_evoked_t(S)  
          S               - input structure  
         fields of S:  
          S.BF        - path to BF.mat file  
          S.act       - active timpeoint(ms) - 1 x 1 matrix      -Default: none  
          S.base      - base timpeoint(ms) - 1 x 1 matrix        -Default: none  
          S.condact   - active condition label - string          -Default: 'ALL'  
          S.condbase  - baseline condition label - string        -Default: 'ALL'  
          S.MNI       - flag to output in MNI space - logical    -Default: true  
          S.summary   - output summary statistic  - logical      -Default: false   
        Output:  
          BF               - path to BF.mat file  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_stat_evoked_t.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bf_stat_evoked_t", *args, **kwargs)
