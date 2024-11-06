from spm.__wrapper__ import Runtime


def _findcluster(*args, **kwargs):
    """
      FINDCLUSTER returns all connected clusters for a three-dimensional six-connected  
        neighborhood  
         
        Use as  
          [cluster, num] = findcluster(onoff, spatdimneighbstructmat, minnbchan)  
        or ar  
          [cluster, num] = findcluster(onoff, spatdimneighbstructmat, spatdimneighbselmat, minnbchan)  
        where  
          onoff                  =  is a 3D boolean matrix with size N1xN2xN3  
          spatdimneighbstructmat =  defines the neighbouring channels/combinations, see below  
          minnbchan              =  the minimum number of neighbouring channels/combinations  
          spatdimneighbselmat    =  is a special neighbourhood matrix that is used for selecting  
                                    channels/combinations on the basis of the minnbchan criterium  
         
        The neighbourhood structure for the first dimension is specified using  
        spatdimneighbstructmat, which is a 2D (N1xN1) matrix. Each row and each column  
        corresponds to a channel (combination) along the first dimension and along that  
        row/column, elements with "1" define the neighbouring channel(s) (combinations).  
        The first dimension of onoff should correspond to the channel(s) (combinations).  
         
        See also SPM_BWLABEL, BWLABEL, BWLABELN  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/findcluster.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("findcluster", *args, **kwargs)
