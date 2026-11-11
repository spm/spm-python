from spm._runtime import Runtime


def _findcluster(*args, **kwargs):
    r"""
      FINDCLUSTER returns all connected clusters for a three-dimensional six-connected  
        neighborhood  
         
        Use as  
          [cluster, num] = findcluster(onoff, connmat, 'minnbchan', minnbchan)  
        or as  
          [cluster, num] = findcluster(onoff, connmat, 'minnbchan', minnbchan, 'spatdimneighbselmat', spatdimneighbselmat)  
        where  
          onoff                  =  is a 3D boolean matrix with size N1xN2xN3  
          connmat                =  defines the neighbouring channels/combinations, see below  
          minnbchan              =  the minimum number of neighbouring channels/combinations  
          spatdimneighbselmat    =  is a special neighbourhood matrix that is used for selecting  
                                    channels/combinations on the basis of the minnbchan criterium  
         
        The neighbourhood structure for the first dimension is specified using  
        connmat, which is a 2D (N1xN1) matrix. Each row and each column  
        corresponds to a channel (combination) along the first dimension and along that  
        row/column, elements with "1" define the neighbouring channel(s) (combinations).  
        The first dimension of onoff should correspond to the channel(s) (combinations).  
         
        See also SPM_BWLABEL, BWLABEL, BWLABELN  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/findcluster.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("findcluster", *args, **kwargs)
