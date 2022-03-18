import numpy as np
import matplotlib.pyplot as plt



encoded = """fd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b6375938003cfd35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b7375938003cfe35b7375a38003cfe35b7375a38003cfe35b7375a38003cfe35b7375a38003cfe35b7375a38003cfe35b7375a38003cfe35b7375a38003cfe35b7375a38003cfe35b7375a38003cfe35b7375a38003cfe35b7375a38003cfe35b7375a38003cfe35b7375a38003cfe35b7375a38003cfe35b7375a38003cfe35b7375a38003cfe35b7375a38003cfe35b7375a38003cfe35b7375a38003cfe35b7375a38003cfe35b7375a38003cfe35b7375a38003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfd35b6375938003cfd35b6375938003cfd35b6375938003cfd35b6375938003cfd35b6375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375838003cfd35b5375838003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b6375938003cfd35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b7375938003cfe35b7375a38003cfe35b7375a38003cfe35b7375a38003cfe35b7375a38003cfe35b7375a38003cfe35b7375a38003cfe35b7375a38003cfe35b7375a38003cfe35b7375a38003cfe35b7375a38003cfe35b7375a38003cfe35b7375a38003cfe35b7375a38003cfe35b7375a38003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfd35b6375938003cfd35b6375938003cfd35b6375938003cfd35b6375938003cfd35b6375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfc35b5375938003cfc35b5375838003cfc35b5375838003cfc35b5375838003cfd35b5375838003cfd35b5375838003cfd35b5375838003cfd35b5375838003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b6375938003cfd35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfd35b6375938003cfd35b6375938003cfd35b6375938003cfd35b6375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfc35b5375938003cfc35b5375838003cfc35b5375838003cfc35b5375838003cfc35b5375838003cfc35b5375838003cfc35b4375838003cfc35b5375838003cfc35b5375838003cfc35b5375838003cfc35b5375838003cfd35b5375838003cfd35b5375838003cfd35b5375838003cfd35b5375838003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b6375938003cfd35b6375938003cfd35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfe35b6375938003cfd35b6375938003cfd35b6375938003cfd35b6375938003cfd35b6375938003cfd35b6375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfc35b5375838003cfc35b5375838003cfc35b5375838003cfc35b5375838003cfc35b5375838003cfc35b5375838003cc82c00331739003cca2c01331739003ccb2c01331739003c3f341f314038003c3f341e314038003c3f341e314038003cfc35b4375838003cfc35b4375838003cfc35b5375838003cfc35b5375838003cfc35b5375838003cfc35b5375838003cfd35b5375838003cfd35b5375838003cfd35b5375838003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b6375938003cfd35b6375938003cfd35b6375938003cfd35b6375938003cfd35b6375938003cfd35b6375938003cfd35b6375938003cfd35b6375938003cfd35b6375938003cfd35b6375938003cfd35b6375938003cfd35b6375938003cfd35b6375938003cfd35b6375938003cfd35b6375938003cfd35b6375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfc35b5375838003cfc35b5375838003cfc35b5375838003cfc35b5375838003cfc35b5375838003cc72cff321639003cc82c00331739003cca2c01331739003ccb2c01331739003ccc2c02331739003cce2c02331739003ccf2c02331739003cd02c03331739003c3f3421314038003c3f3420314038003c3f3420314038003c3f341f314038003c3f341f314038003c3f341e314038003c3f341e314038003cfc35b4375838003cfc35b4375838003cfc35b5375838003cfc35b5375838003cfc35b5375838003cfc35b5375838003cfc35b5375838003cfd35b5375838003cfd35b5375838003cfd35b5375838003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375938003cfd35b5375838003cfc35b5375838003cfc35b5375838003cfc35b5375838003cfc35b5375838003cc72cff321639003cc82c00331639003cc92c00331739003cca2c01331739003ccc2c02331739003ccd2c02331739003cce2c02331739003cd02c02331739003cd12c03331739003cd22c03331739003cd32c04331739003cd42c04331739003cd62c04331739003c403424314138003c403423314138003c3f3423314138003c3f3422314138003c3f3422314038003c3f3421314038003c3f3420314038003c3f3420314038003c3f341f314038003c3f341f314038003cfc35b4375838003cfc35b4375838003cfc35b4375838003cfc35b4375838003cfc35b5375838003cfc35b5375838003cfc35b5375838003cfc35b5375838003cfc35b5375838003cfc35b5375838003cfc35b5375838003cfd35b5375838003cfd35b5375838003cfd35b5375838003cfd35b5375838003cfd35b5375838003cfd35b5375838003cfd35b5375838003cfd35b5375838003cfd35b5375838003cfd35b5375838003cfd35b5375838003cfc35b5375838003cfc35b5375838003cfc35b5375838003cfc35b5375838003cfc35b5375838003cc72cff321639003cc82cff321639003cc92c00331639003cca2c00331739003ccb2c01331739003ccc2c01331739003cce2c02331739003ccf2c02331739003cd02c02331739003cd12c03331739003cd22c03331739003cd32c04331739003cd42c04331739003cd52c04331739003cd72c04331739003cd82c05331739003cd92c05331739003cda2c06331739003cdb2c06331739003c403426314138003c403426314138003c403425314138003c403425314138003c403424314138003c403424314138003c403423314138003c3f3423314138003c3f3422314138003c3f3422314038003c3f3421314038003c3f3420314038003c3f3420314038003cfc35b4375838003cfc35b4375838003cfc35b4375838003cfc35b4375838003cfc35b4375838003cfc35b4375838003cfc35b4375838003cfc35b4375838003cfc35b4375838003cfc35b5375838003cfc35b5375838003cfc35b5375838003cfc35b5375838003cfc35b5375838003cfc35b5375838003cfc35b5375838003cfc35b5375838003cfc35b5375838003cfc35b5375838003ccb2c01331739003ccb2c01331739003ccc2c01331739003ccc2c01331739003cce2c02331739003cce2c02331739003ccf2c02331739003cd02c02331739003cd12c02331739003cd22c03331739003cd32c03331739003cd42c04331739003cd52c04331739003cd62c04331739003cd72c04331739003cd82c05331739003cd92c05331739003cda2c06331739003cdc2c06331739003cdc2c07331739003cdd2c07331739003cde2c07331739003cdf2c07331739003ce02c07331739003c413428314138003c403428314138003c403428314138003c403427314138003c403427314138003c403426314138003c403426314138003c403425314138003c403425314138003c403425314138003c403424314138003c403424314138003c403423314138003c3f3423314138003c3f3422314138003c3f3422314038003cfc35b3375838003cfc35b3375838003cfc35b3375838003cfc35b4375838003cfc35b4375838003cfc35b4375838003cfc35b4375838003cfc35b4375838003cfc35b4375838003cfc35b4375838003cd32c03331739003cd32c03331739003cd32c03331739003cd32c03331739003cd32c03331739003cd32c03331739003cd32c03331739003cd32c03331739003cd42c03331739003cd42c04331739003cd52c04331739003cd62c04331739003cd62c04331739003cd72c04331739003cd82c04331739003cd92c05331739003cda2c05331739003cdb2c06331739003cdc2c06331739003cdd2c07331739003cde2c07331739003cdf2c07331739003cdf2c07331739003ce02c07331739003ce12c08331739003ce22c08331739003ce32c09331739003ce42c09331739003ce52c09331739003ce62c0a331739003c41342b314138003c41342a314138003c41342a314138003c41342a314138003c413429314138003c413429314138003c413429314138003c413428314138003c403428314138003c403427314138003c403427314138003c403427314138003c403426314138003c403426314138003c403425314138003c403425314138003c403425314138003c403424314138003c403424314138003c403424314138003cfc35b3375838003cde2c06331739003cdd2c06331739003cdd2c06331739003cdc2c05331739003cdc2c05331739003cdb2c05331739003cdb2c05331739003cdb2c05331739003cdb2c05331739003cdb2c05331739003cdb2c05331739003cdb2c05331739003cdc2c06331739003cdc2c06331739003cdc2c06331739003cdd2c06331739003cdd2c07331739003cde2c07331739003cdf2c07331739003cdf2c07331739003ce02c07331739003ce12c07331739003ce22c08331739003ce32c08331739003ce32c09331739003ce42c09331739003ce52c09331739003ce62c0a331739003ce72c0a331739003ce82c0a331739003ce92c0a331739003ce92c0a331739003cea2c0a331739003ceb2c0b331739003cec2c0b331739003c41342d314138003c41342d314138003c41342d314138003c41342c314138003c41342c314138003c41342c314138003c41342b314138003c41342b314138003c41342b314138003c41342a314138003c41342a314138003c41342a314138003c413429314138003c413429314138003c413429314138003c413428314138003c403428314138003c403428314138003c403427314138003c403427314138003ce72c09331739003ce72c09331739003ce62c08331739003ce52c08331739003ce42c08331739003ce42c08331739003ce42c08331739003ce32c08331739003ce32c08331739003ce32c08331739003ce32c08331739003ce32c08331739003ce32c08331739003ce42c08331739003ce42c08331739003ce42c08331739003ce52c09331739003ce62c09331739003ce62c09331739003ce72c0a331739003ce72c0a331739003ce82c0a331739003ce92c0a331739003ce92c0a331739003cea2c0a331739003ceb2c0b331739003ceb2c0b331739003cec2c0b331739003ced2c0b331739003ced2c0c331739003cee2c0c331739003cef2c0c331739003cef2c0c331739003cf02c0c331739003cf12c0c331739003cf12c0d331739003c423430314238003c42342f314238003c41342f314238003c41342f314238003c41342f314238003c41342e314138003c41342e314138003c41342e314138003c41342e314138003c41342d314138003c41342d314138003c41342d314138003c41342c314138003c41342c314138003c41342c314138003c41342c314138003c41342b314138003c41342b314138003c41342b314138003c41342b314138003cf02c0b331739003cef2c0b331739003cee2c0b331739003cee2c0b331739003ced2c0b331739003ced2c0b331739003ced2c0a331739003cec2c0a331739003cec2c0a331739003cec2c0a331739003cec2c0a331739003cec2c0a331739003cec2c0b331739003cec2c0b331739003ced2c0b331739003ced2c0b331739003ced2c0b331739003ced2c0b331739003cee2c0c331739003cef2c0c331739003cef2c0c331739003cef2c0c331739003cf02c0c331739003cf02c0c331739003cf12c0c331739003cf22c0d331739003cf22c0d331739003cf32c0d331739003cf32c0d331739003cf42c0e331839003cf42c0e331839003cf52c0e331839003cf52c0e331839003cf62c0f331839003cf62c0f331839003cf72c0f331839003c423432314238003c423432314238003c423432314238003c423431314238003c423431314238003c423431314238003c423431314238003c423431314238003c423430314238003c423430314238003c423430314238003c423430314238003c423430314238003c42342f314238003c42342f314238003c41342f314238003c41342f314238003c41342e314238003c41342e314138003c41342e314138003cf82c0e331839003cf72c0e331739003cf72c0e331739003cf72c0e331739003cf62c0d331739003cf62c0d331739003cf52c0d331739003cf52c0d331739003cf52c0d331739003cf52c0d331739003cf52c0d331739003cf52c0d331739003cf52c0d331739003cf52c0d331739003cf52c0e331739003cf52c0e331839003cf52c0e331839003cf62c0e331839003cf62c0e331839003cf62c0e331839003cf62c0e331839003cf72c0f331839003cf72c0f331839003cf82c0f331839003cf82c0f331839003cf82c0f331839003cf92c0f331839003cf92c0f331839003cfa2c0f331839003cfa2c0f331839003cfb2c10331839003cfb2c10331839003cfb2c10331839003cfc2c10331839003cfc2c10331839003cfc2c11331839003c433435314238003c423435314238003c423434314238003c423434314238003c423434314238003c423434314238003c423434314238003c423434314238003c423434314238003c423433314238003c423433314238003c423433314238003c423433314238003c423433314238003c423433314238003c423432314238003c423432314238003c423432314238003c423432314238003c423432314238003c002d11331839003c002d11331839003c002d10331839003cff2c10331839003cff2c10331839003cff2c10331839003cfe2c10331839003cfe2c10331839003cfe2c10331839003cfe2c10331839003cfe2c10331839003cfd2c10331839003cfe2c10331839003cfe2c10331839003cfd2c10331839003cfe2c10331839003cfe2c10331839003cfe2c11331839003cfe2c11331839003cfe2c11331839003cfe2c11331839003cff2c11331839003cff2c11331839003cff2c11331839003cff2c11331839003c002d11331839003c002d11331839003c002d11331839003c002d11331839003c012d11331839003c012d11331839003c012d12331839003c012d12331839003c022d12331839003c022d12331839003c022d12331839003c433437314238003c433437314238003c433437314238003c433437314238003c433437314238003c433437314238003c433437314238003c433437314238003c433437314238003c433436314238003c433436314238003c433436314238003c433436314238003c433436314238003c433436314238003c433436314238003c433436314238003c433436314238003c433436314238003c433436314238003c092d13331839003c092d13331839003c082d13331839003c082d13331839003c082d13331839003c072d13331839003c072d13331839003c072d13331839003c072d13331839003c072d13331839003c062d13331839003c062d13331839003c062d13331839003c062d13331839003c062d13331839003c062d13331839003c062d13331839003c062d13331839003c062d13331839003c062d13331839003c062d13331839003c062d14331839003c062d14331839003c072d14331839003c072d14331839003c072d14331839003c072d14331839003c072d14331839003c072d14331839003c072d14331839003c072d14331839003c072d14331839003c072d14331839003c082d14331839003c082d14331839003c082d14331839003c43343a314238003c43343a314238003c43343a314238003c43343a314238003c43343a314238003c43343a314238003c43343a314238003c43343a314238003c43343a314238003c43343a314238003c433439314238003c433439314238003c433439314238003c433439314238003c433439314238003c433439314238003c433439314238003c433439314238003c433439314238003c433439314238003c112d16331839003c112d16331839003c112d16331839003c102d16331839003c102d16331839003c102d16331839003c102d16331839003c102d16331839003c102d16331839003c102d16331839003c0f2d16331839003c0f2d16331839003c0f2d16331839003c0f2d16331839003c0f2d16331839003c0f2d16331839003c0e2d16331839003c0e2d16331839003c0e2d16331839003c0e2d16331839003c0e2d16331839003c0e2d16331839003c0e2d16331839003c0e2d16331839003c0e2d16331839003c0e2d16331839003c0e2d16331839003c0e2d16331839003c0e2d16331839003c0e2d16331839003c0e2d16331839003c0e2d16331839003c0e2d16331839003c0e2d16331839003c0e2d16331839003c0e2d16331839003c44343c314338003c44343c314338003c44343c314338003c44343c314338003c44343c314338003c44343c314338003c44343d314338003c44343d314338003c44343d314338003c44343d314338003c44343d314338003c44343d314338003c44343d314338003c44343d314338003c44343d314338003c44343d314338003c44343d314338003c44343d314338003c44343d314338003c44343d314338003c1a2d19331939003c1a2d19331939003c1a2d19331939003c192d19331939003c192d19331939003c192d19331939003c192d19331939003c192d19331939003c182d19331939003c182d19331939003c182d19331939003c182d19331939003c182d19331939003c172d19331939003c172d19331939003c172d19331939003c172d19331939003c162d19331939003c162d19331939003c162d19331939003c162d19331939003c162d18331939003c152d18331939003c152d18331939003c152d18331939003c152d18331939003c152d18331939003c142d18331939003c142d18331939003c142d18331939003c142d18331939003c142d18331939003c142d18331939003c132d18331939003c132d18331939003c132d18331939003c44343f314338003c44343f314338003c44343f314338003c44343f314338003c44343f314338003c44343f314338003c44343f314338003c44343f314338003c443440314338003c443440314338003c443440314338003c443440314338003c443440314338003c443440314338003c443440314338003c443440314338003c443440314338003c443440314338003c443441314338003c443441314338003c222d1b331939003c222d1b331939003c222d1b331939003c222d1b331939003c222d1b331939003c222d1b331939003c222d1b331939003c222d1b331939003c222d1b331939003c212d1b331939003c212d1b331939003c212d1b331939003c212d1b331939003c202d1b331939003c202d1b331939003c1f2d1b331939003c1f2d1b331939003c1f2d1b331939003c1e2d1b331939003c1e2d1b331939003c1e2d1b331939003c1d2d1b331939003c1d2d1b331939003c1c2d1b331939003c1c2d1a331939003c1c2d1a331939003c1b2d1a331939003c1b2d1a331939003c1b2d1a331939003c1a2d1a331939003c1a2d1a331939003c1a2d1a331939003c1a2d1a331939003c192d19331939003c192d19331939003c192d19331939003c453441314338003c453442314338003c453442314338003c453442314338003c453442314338003c453442314338003c453442314338003c453442314338003c453443314338003c453443314338003c453443314338003c453443314338003c453443314338003c453443314338003c453443314338003c453444314338003c453444314338003c453444314338003c453444314338003c453444314338003c2a2d1e331939003c2b2d1e331939003c2a2d1e331939003c2a2d1e331939003c2a2d1e331939003c2a2d1e331939003c2a2d1e331939003c2a2d1e331939003c2a2d1e331939003c2a2d1e331939003c292d1e331939003c292d1e331939003c292d1e331939003c282d1e331939003c282d1e331939003c272d1e331939003c272d1e331939003c272d1e331939003c262d1e331939003c262d1e331939003c262d1d331939003c252d1d331939003c242d1d331939003c242d1d331939003c232d1d331939003c232d1c331939003c222d1c331939003c222d1c331939003c212d1c331939003c212d1c331939003c212d1c331939003c202d1b331939003c202d1b331939003c1f2d1b331939003c1f2d1b331939003c1f2d1b331939003c453444314338003c453444314338003c453444314338003c453444314338003c453445314338003c453445314338003c453445314338003c453445314338003c453445314338003c453446314338003c453446314338003c453446314338003c453446314338003c453447314338003c453447314338003c453447314438003c453447314438003c453448314438003c453448314438003cc639f13aa93b003cc439f03aa93b003cc139ef3aa83b003c332d20331939003c332d21331939003c332d21331939003c332d21331939003c332d21331939003c332d21331939003c332d21331939003c322d21331939003c322d21331939003c322d20331939003c312d20331939003c312d20331939003c302d20331939003c302d20331939003c2f2d20331939003c2e2d20331939003c2e2d20331939003c2d2d20331939003c2d2d20331939003c2c2d20331939003c2b2d1f331939003c2b2d1f331939003c2a2d1f331939003c292d1f331939003c292d1e331939003c282d1e331939003c282d1e331939003c272d1e331939003c272d1e331939003c262d1e331939003c262d1e331939003c252d1e331939003c252d1d331939003c242d1d331939003c453446314338003c453447314338003c453447314338003c453447314438003c453447314438003c453448314438003c453448314438003c463448314438003c463448314438003c463449314438003c463449314438003c463449314438003c46344a314438003cae39e73aa43b003caa39e63aa43b003ca739e53aa33b003ca439e43aa33b003ca139e33aa33b003c9f39e23aa23b003c9d39e13aa13b003c9c39e03aa13b003c9b39df3aa13b003c9939df3aa13b003c9739de3aa03b003c9639dd3aa03b003c9539dd3a9f3b003c9539dd3a9f3b003c9439dc3a9f3b003c9439dc3a9f3b003c9539dd3a9f3b003c9539dd3a9f3b003c9639dd3aa03b003c392d23331939003c392d23331939003c382d23331939003c372d23331939003c372d23331939003c362d23331939003c362d23331939003c352d22331939003c342d22331939003c332d22331939003c332d22331939003c322d21331939003c312d21331939003c302d21331939003c2f2d20331939003c2f2d20331939003c2e2d20331939003c2d2d20331939003c2d2d20331939003c2c2d20331939003c2b2d20331939003c2b2d1f331939003c2a2d1f331939003c292d1f331939003c463449314438003c463449314438003c463449314438003c46344a314438003c46344a314438003c46344a314438003c46344b314438003ca439e23aa23b003ca039e13aa13b003c9d39e03aa13b003c9939df3aa13b003c9639dd3a9f3b003c9239dc3a9f3b003c8f39da3a9f3b003c8d39d93a9f3b003c8939d93a9e3b003c8739d93a9d3b003c8439d73a9d3b003c8139d63a9d3b003c8039d53a9c3b003c7e39d43a9c3b003c7d39d33a9c3b003c7c39d23a9c3b003c7a39d23a9c3b003c7839d23a9c3b003c7739d23a9c3b003c7639d23a9c3b003c7639d23a9c3b003c7639d23a9c3b003c7639d23a9c3b003c7739d23a9c3b003c7839d23a9c3b003c7a39d23a9c3b003c7c39d23a9c3b003c7d39d33a9c3b003c7e39d43a9c3b003c8039d53a9c3b003c8139d63a9d3b003c8439d73a9d3b003c8739d93a9d3b003c8939d93a9e3b003c8b39d93a9f3b003c392d24331a39003c382d23331a39003c372d23331939003c362d23331939003c362d23331939003c352d23331939003c342d23331939003c342d22331939003c332d22331939003c322d21331939003c312d21331939003c302d21331939003c302d21331939003c2f2d20331939003c46344b314438003c9e39e03aa13b003c9b39df3aa13b003c9739dd3aa13b003c9439dd3aa03b003c9239dd3a9f3b003c8d39db3a9f3b003c8a39da3a9e3b003c8639d83a9d3b003c8439d63a9d3b003c8039d53a9c3b003c7d39d43a9c3b003c7a39d43a9c3b003c7639d23a9c3b003c7439d03a9a3b003c7239d03a9a3b003c7039d03a9a3b003c6e39ce3a9a3b003c6c39cd3a9a3b003c6a39cc3a9a3b003c6939cc3a993b003c6739cc3a983b003c6639ca3a983b003c6539ca3a983b003c6439c93a983b003c6339c93a983b003c6239c93a983b003c6239c93a983b003c6239c93a983b003c6239c93a983b003c6339c93a983b003c6439c93a983b003c6539ca3a983b003c6639ca3a983b003c6739cc3a983b003c6939cc3a993b003c6a39cc3a9a3b003c6c39cd3a9a3b003c6e39ce3a9a3b003c7039d03a9a3b003c7239d03a9a3b003c7439d03a9a3b003c7639d23a9c3b003c7a39d23a9c3b003c7d39d33a9c3b003c7f39d53a9c3b003c8239d63a9d3b003c8639d83a9d3b003c8839d93a9e3b003c8b39d93a9f3b003c8f39db3a9f3b003c9339dc3a9f3b003c362d23331939003c362d23331939003c352d23331939003c342d23331939003c8f39da3a9f3b003c8a39d93a9d3b003c8639d73a9d3b003c8339d63a9d3b003c8139d63a9d3b003c7c39d43a9c3b003c7939d33a9c3b003c7739d23a9c3b003c7439d03a9b3b003c6f39cf3a9a3b003c6d39ce3a9a3b003c6a39ce3a9a3b003c6839cc3a983b003c6639cc3a983b003c6339ca3a983b003c6139c93a983b003c5e39c93a983b003c5c39c83a963b003c5a39c73a963b003c5839c73a963b003c5839c63a963b003c5739c53a963b003c5639c53a963b003c5539c53a963b003c5439c53a963b003c5339c53a963b003c5239c53a963b003c5239c43a953b003c5239c43a953b003c5239c53a963b003c5339c53a963b003c5439c53a963b003c5539c53a963b003c5639c53a963b003c5739c53a963b003c5839c63a963b003c5839c73a963b003c5a39c73a963b003c5c39c83a963b003c5e39c93a983b003c6139c93a983b003c6339c93a983b003c6639ca3a983b003c6839cc3a983b003c6a39cc3a9a3b003c6d39ce3a9a3b003c6f39cf3a9a3b003c7239d03a9a3b003c7439d13a9b3b003c7739d23a9c3b003c7c39d23a9c3b003c7e39d43a9c3b003c8039d53a9d3b003c8339d73a9d3b003c8739d93a9d3b003c8939d93a9f3b003c7d39d43a9c3b003c7a39d43a9c3b003c7839d23a9b3b003c7339d03a9a3b003c7039d03a9a3b003c6e39ce3a9a3b003c6b39ce3a993b003c6939cc3a983b003c6439ca3a983b003c6139c93a983b003c5e39c93a973b003c5b39c73a963b003c5b39c73a963b003c5839c53a963b003c5539c53a963b003c5339c53a963b003c5039c33a953b003c4f39c33a943b003c4e39c33a943b003c4c39c23a943b003c4c39c13a943b003c4b39c13a943b003c4939c13a943b003c4939c13a943b003c4939c13a943b003c4939c13a943b003c4839c13a943b003c4839c13a943b003c4839c13a943b003c4839c13a943b003c4939c13a943b003c4939c13a943b003c4939c13a943b003c4939c13a943b003c4b39c13a943b003c4c39c13a943b003c4c39c23a943b003c4e39c33a943b003c4f39c33a943b003c5039c33a953b003c5339c53a963b003c5539c53a963b003c5839c53a963b003c5839c73a963b003c5b39c73a963b003c5e39c93a973b003c6039c93a983b003c6339c93a983b003c6639ca3a983b003c6839cc3a993b003c6b39cc3a9a3b003c6d39ce3a9a3b003c7039d03a9a3b003c7339d03a9a3b003c7539d23a9b3b003c7839d23a9c3b003c7039d03a9a3b003c6e39ce3a9a3b003c6b39ce3a993b003c6939cc3a983b003c6639cc3a983b003c6239c93a983b003c5e39c93a973b003c5c39c73a963b003c5a39c73a963b003c5739c53a963b003c5439c53a963b003c5139c43a953b003c4f39c33a943b003c4c39c33a943b003c4b39c13a943b003c4939c13a943b003c4839c13a943b003c4639c03a943b003c4639be3a923b003c4339be3a923b003c4339be3a923b003c4239be3a923b003c4039be3a923b003c4039be3a923b003c4039be3a923b003c4039bd3a923b003c4039bd3a923b003c4039bd3a923b003c4039bd3a923b003c4039bd3a923b003c4039bd3a923b003c4039be3a923b003c4039be3a923b003c4039be3a923b003c4239be3a923b003c4339be3a923b003c4339be3a923b003c4639be3a923b003c4639c03a943b003c4839c13a943b003c4939c13a943b003c4b39c13a943b003c4c39c23a943b003c4e39c33a943b003c4f39c33a943b003c5139c43a953b003c5439c53a963b003c5739c53a963b003c5839c63a963b003c5a39c73a963b003c5d39c83a973b003c6039c93a983b003c6339c93a983b003c6539ca3a983b003c6839cc3a983b003c6a39cc3a9a3b003c6739cc3a983b003c6439cc3a983b003c6139c93a983b003c5e39c93a963b003c5b39c73a963b003c5839c73a963b003c5539c53a963b003c5539c53a953b003c5239c33a943b003c4e39c33a943b003c4c39c23a943b003c4939c13a943b003c4739c13a943b003c4639bf3a933b003c4339be3a923b003c4339be3a923b003c4039be3a923b003c4039bc3a923b003c3e39bc3a923b003c3d39bc3a923b003c3d39bc3a923b003c3c39bc3a923b003c3a39bc3a923b003c3a39bc3a923b003c3a39bc3a923b003c3a39bc3a923b003c3a39bb3a913b003c3a39bb3a913b003c3a39bb3a913b003c3a39bb3a913b003c3a39bc3a923b003c3a39bc3a923b003c3a39bc3a923b003c3a39bc3a923b003c3c39bc3a923b003c3d39bc3a923b003c3d39bc3a923b003c3e39bc3a923b003c4039bc3a923b003c4039be3a923b003c4039be3a923b003c4339be3a923b003c4439be3a923b003c4639bf3a933b003c4739c13a943b003c4939c13a943b003c4b39c13a943b003c4c39c23a943b003c4f39c33a943b003c4f39c33a943b003c5239c53a963b003c5539c53a963b003c5839c53a963b003c5839c73a963b003c5b39c73a963b003c5e39c93a983b003c6139c93a983b003c5e39c93a963b003c5d39c73a963b003c5a39c73a963b003c5739c63a963b003c5439c53a953b003c5039c33a943b003c4f39c33a943b003c4c39c13a943b003c4939c13a943b003c4639c03a923b003c4339be3a923b003c4139be3a923b003c4039bc3a923b003c3d39bc3a923b003c3d39bc3a923b003c3c39bc3a923b003c3a39bb3a913b003c3a39ba3a903b003c3939ba3a903b003c3739ba3a903b003c3739ba3a903b003c3739ba3a903b003c3739ba3a903b003c3739ba3a903b003c3739ba3a903b003c3739ba3a903b003c3739ba3a903b003c3739ba3a903b003c3739ba3a903b003c3739ba3a903b003c3739ba3a903b003c3739ba3a903b003c3739ba3a903b003c3739ba3a903b003c3739ba3a903b003c3939ba3a903b003c3a39ba3a903b003c3a39bb3a913b003c3a39bc3a923b003c3c39bc3a923b003c3d39bc3a923b003c3d39bc3a923b003c4039bd3a923b003c4039be3a923b003c4239be3a923b003c4339be3a923b003c4639be3a923b003c4739c13a943b003c4939c13a943b003c4a39c13a943b003c4c39c23a943b003c4e39c33a943b003c4f39c33a943b003c5239c43a953b003c5539c53a963b003c5e39c93a963b003c5e39c83a963b003c5b39c73a963b003c5839c73a963b003c5539c53a943b003c5239c33a943b003c4f39c33a943b003c4b39c13a943b003c4739c13a923b003c4639be3a923b003c4339be3a923b003c4039bd3a923b003c3d39bc3a923b003c3d39bc3a923b003c3a39bc3a903b003c3a39ba3a903b003c3739ba3a903b003c3739ba3a903b003c3739ba3a903b003c3539ba3a903b003c3439ba3a903b003c3439ba3a903b003c3439b93a903b003c3439b83a903b003c3439b83a903b003c3439b83a903b003c3439b83a903b003c3439b83a903b003c3439b83a903b003c3439b83a903b003c3439b83a903b003c3439b83a903b003c3439b83a903b003c3439b93a903b003c3439ba3a903b003c3439ba3a903b003c3539ba3a903b003c3739ba3a903b003c3739ba3a903b003c3739ba3a903b003c3739ba3a903b003c3939ba3a903b003c3a39ba3a903b003c3a39bc3a923b003c3c39bc3a923b003c3d39bc3a923b003c3d39bc3a923b003c4039bd3a923b003c4039be3a923b003c4339be3a923b003c4339be3a923b003c4639be3a923b003c4739c13a943b003c4939c13a943b003c4b39c13a943b003c4c39c23a943b003c6139c93a963b003c5e39c93a963b003c5b39c73a963b003c5739c73a953b003c5339c53a943b003c4f39c33a943b003c4c39c33a943b003c4939c13a933b003c4639be3a923b003c4339be3a923b003c4039bd3a923b003c3d39bc3a923b003c3a39bc3a913b003c3a39ba3a903b003c3739ba3a903b003c3739ba3a903b003c3539ba3a903b003c3439ba3a903b003c3439b83a903b003c3439b83a903b003c3439b83a903b003c3239b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c3239b83a903b003c3439b83a903b003c3439b83a903b003c3439b83a903b003c3439b83a903b003c3439ba3a903b003c3439ba3a903b003c3639ba3a903b003c3739ba3a903b003c3739ba3a903b003c3739ba3a903b003c3a39ba3a903b003c3a39bb3a913b003c3a39bc3a923b003c3d39bc3a923b003c3d39bc3a923b003c3f39bc3a923b003c4039be3a923b003c4139be3a923b003c4339be3a923b003c4539be3a923b003c4639c03a943b003c6439cc3a963b003c6139c93a963b003c5e39c93a963b003c5a39c73a953b003c5639c53a943b003c5239c43a943b003c4c39c33a943b003c4939c13a923b003c4639be3a923b003c4039be3a923b003c3e39bc3a923b003c3a39bc3a903b003c3a39ba3a903b003c3739ba3a903b003c3739ba3a903b003c3439ba3a903b003c3439b83a903b003c3439b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c3239b83a903b003c3439b83a903b003c3439b83a903b003c3439b83a903b003c3439ba3a903b003c3439ba3a903b003c3739ba3a903b003c3739ba3a903b003c3739ba3a903b003c3939ba3a903b003c3a39ba3a903b003c3a39bc3a923b003c3c39bc3a923b003c3d39bc3a923b003c3e39bc3a923b003c4039bd3a923b003c4039be3a923b003c6a39ce3a983b003c6739cc3a963b003c6339cb3a963b003c5e39c93a963b003c5939c73a953b003c5439c53a943b003c4f39c33a943b003c4a39c13a923b003c4639be3a923b003c4039be3a923b003c3d39bc3a923b003c3a39bc3a903b003c3739ba3a903b003c3739ba3a903b003c3439ba3a903b003c3439b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c2e39b83a903b003c2e39b83a903b003c2e39b83a903b003c2e39b83a903b003c2e39b83a903b003c2e39b83a903b003c2e39b83a903b003c2e39b83a903b003c2e39b83a903b003c2e39b83a903b003c2f39b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c3139b83a903b003c3439b83a903b003c3439b83a903b003c3439b83a903b003c3439ba3a903b003c3439ba3a903b003c3739ba3a903b003c3739ba3a903b003c3739ba3a903b003c3939ba3a903b003c3a39ba3a903b003c3a39bc3a923b003c3c39bc3a923b003c3d39bc3a923b003c"""

raw_data = [5, 49, 230, 49, 198, 50, 0, 60, 5, 49, 230, 49, 198, 50, 0, 60, 87, 57, 197, 58, 150, 59, 0, 60, 87, 57, 197, 58, 150, 59, 0, 60]
#encoded = "0531e631c632003c0531e631c632003c5739c53a963b003c5739c53a963b003c"
b = bytes.fromhex(encoded)
print(b)
result = np.frombuffer(b, dtype=np.float16).reshape((32,56,4)).astype(np.float32)

print(result.shape)

plt.imshow(result[:,:,:3])
plt.show()