from spm.__wrapper__ import Runtime, MatlabClassWrapper


class nifti(MatlabClassWrapper):
    def __init__(self, *args, _objdict=None, **kwargs):
        """
          Create a NIFTI-1 object  
           __________________________________________________________________________  
            
              Documentation for nifti  
                 doc nifti  
            
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@nifti/nifti.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        if _objdict is None:
            _objdict = Runtime.call("nifti", *args, **kwargs)
            
        super().__init__(_objdict)

    def _M2Q(self, *args, **kwargs):
        """
          Convert from rotation matrix to quaternion form  
            See: http://skal.planet-d.net/demo/matrixfaq.htm  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@nifti/private/M2Q.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("M2Q", *args, **kwargs)

    def _Q2M(self, *args, **kwargs):
        """
          Generate a rotation matrix from a quaternion xi+yj+zk+w,  
            where Q = [x y z], and w = 1-x^2-y^2-z^2.  
            See: http://skal.planet-d.net/demo/matrixfaq.htm  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@nifti/private/Q2M.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("Q2M", *args, **kwargs)

    def _decode_qform0(self, *args, **kwargs):
        """
          Decode qform info from NIFTI-1 headers.  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@nifti/private/decode_qform0.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("decode_qform0", *args, **kwargs)

    def _empty_hdr(self, *args, **kwargs):
        """
          Create an empty NIFTI header  
            FORMAT hdr = empty_hdr  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@nifti/private/empty_hdr.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("empty_hdr", *args, **kwargs)

    def _encode_qform0(self, *args, **kwargs):
        """
          Encode an affine transform into qform  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@nifti/private/encode_qform0.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("encode_qform0", *args, **kwargs)

    def _findindict(self, *args, **kwargs):
        """
          Look up an entry in the dictionary  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@nifti/private/findindict.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("findindict", *args, **kwargs)

    def _getdict(self, *args, **kwargs):
        """
          Dictionary of NIFTI stuff  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@nifti/private/getdict.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("getdict", *args, **kwargs)

    def _mayo2nifti1(self, *args, **kwargs):
        """
          Convert from an ANALYZE to a NIFTI-1 header  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@nifti/private/mayo2nifti1.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("mayo2nifti1", *args, **kwargs)

    def _mayostruc(self, *args, **kwargs):
        """
          Create a data structure describing Analyze headers  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@nifti/private/mayostruc.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("mayostruc", *args, **kwargs)

    def _nifti1struc(self, *args, **kwargs):
        """
          Create a data structure describing NIFTI-1 headers  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@nifti/private/nifti1struc.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("nifti1struc", *args, **kwargs)

    def _nifti2struc(self, *args, **kwargs):
        """
          Create a data structure describing NIFTI-2 headers  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@nifti/private/nifti2struc.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("nifti2struc", *args, **kwargs)

    def _nifti_stats(self, *args, **kwargs):
        """
          Conversion among various statistics  
            FORMAT P = nifti_stats(VAL,CODE,OPT,PARAM)  
              CODE can be one of  
                'CORREL'      'TTEST'       'FTEST'       'ZSCORE'  
                'CHISQ'       'BETA'        'BINOM'       'GAMMA'  
                'POISSON'     'NORMAL'      'FTEST_NONC'  'CHISQ_NONC'  
                'LOGISTIC'    'LAPLACE'     'UNIFORM'     'TTEST_NONC'  
                'WEIBULL'     'CHI'         'INVGAUSS'    'EXTVAL'  
                'PVAL'  
              With only one input argument, CODE defaults to 'ZSCORE'  
             
              OPT can be one of  
                '-p' ==> output P = Prob(statistic < VAL).  
                '-q' ==> output is 1-p.  
                '-d' ==> output is probability density.  
                '-1' ==> output is X such that Prob(statistic < x) = VAL.  
                '-z' ==> output is Z such that Normal cdf(Z) = p(VAL).  
                '-h' ==> output is Z such that 1/2-Normal cdf(Z) = p(VAL).  
              With less than three input arguments, OPT defaults to '-p'.  
             
              PARAM are up to three distribution parameters.  
              These default to zero if unspecified.  
             
              P is an array with the same dimensions as VAL.  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@nifti/private/nifti_stats.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("nifti_stats", *args, **kwargs)

    def _niftistruc(self, *args, **kwargs):
        """
          Create a data structure describing NIFTI headers  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@nifti/private/niftistruc.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("niftistruc", *args, **kwargs)

    def _read_extras(self, *args, **kwargs):
        """
          Read extra bits of information  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@nifti/private/read_extras.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("read_extras", *args, **kwargs)

    def _read_hdr(self, *args, **kwargs):
        """
          Get a variety of information from a NIFTI header  
            FORMAT vol = read_hdr(fname)  
            fname      - filename of image  
            vol        - various bits of information  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@nifti/private/read_hdr.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("read_hdr", *args, **kwargs)

    def _read_hdr_raw(self, *args, **kwargs):
        """
          Read a NIFTI header  
            FORMAT [hdr,be] = read_hdr_raw(hname)  
            hname - filename of image's header  
            hdr   - a structure containing header info  
            be    - whether big-endian or not  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@nifti/private/read_hdr_raw.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("read_hdr_raw", *args, **kwargs)

    def _write_extras(self, *args, **kwargs):
        """
          Write extra bits of information  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@nifti/private/write_extras.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("write_extras", *args, **kwargs)

    def _write_hdr_raw(self, *args, **kwargs):
        """
          Write a NIFTI-1 header  
            FORMAT sts = write_hdr_raw(fname,hdr,be)  
            fname      - filename of image  
            hdr        - a structure containing hdr info  
            be         - whether big-endian or not [Default: native]  
             
            sts        - status (1=good, 0=bad)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@nifti/private/write_hdr_raw.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("write_hdr_raw", *args, **kwargs)
